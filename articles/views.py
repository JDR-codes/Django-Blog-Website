from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . models import *
from likes_comments.models import *
from user_profile.models import *
from . forms import ArticleForm
# Create your views here.

# Public Feed
# list all the articles

def articles_list_view(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        return redirect('user_create')
    articles = Article.objects.filter(author__in = profile.following.all())
    print(articles)
    context = {
        'articles' : articles
    }
    return render(request,'article_list.html',context)


# list all the categories
def category_list_view(request):
    context = {
        'categories': Category.objects.all()
    } 
    return render(request,'categories.html',context)

# list all the articles under a specific category
def category_post_view(request,id):
    context = {}
    posts = Article.objects.filter(category = id)
    if posts:
        context['posts'] = posts
    else:
        context['error'] = 'No posts under this category !!'
    print(context)
    return render(request,'category_post.html',context)


# button (my blogs/my article), when clicked on this
# show only the logged-in users articles
@login_required(login_url='login')
def user_article_list_views(request):
    context = {
        'articles' : Article.objects.filter(author = request.user)
    }
    return render(request,'user_articles.html',context)
    


# Show full details of a blog post / article when clicked on it
def article_details_view(request,id):
    article = Article.objects.get(id = id)
    try:
        likes = Like.objects.get(post = article.id)
    except:
        likes = 0
    context = {
        'article' : article,
        'likes' : likes
    }
    return render(request,'article_details.html',context)

# Allow only logged-in user to create a new article
@login_required(login_url='login')
def article_create_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            author =request.user
            form.create(author)
            return redirect ('articles-list')
        
    form = ArticleForm()
    return render(request,'create_article.html',{'form' : form})

# allow only logged-in user to update only his own article
# user must not be able to edit anything from other users article/blog post
@login_required(login_url='login')
def article_update_view(request,id):
    
    details = Article.objects.get(id = id, author = request.user)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.update(details)
            return redirect ('article-details',id)
    
    form = ArticleForm(initial={
        'category' : details.category,
        'title' : details.title,
        'content' : details.content,

    })
    return render(request,'update_details.html',{'form' : form})

# Allow user to delete the article which only belongs to them.
@login_required(login_url='login')
def article_delete_view(request,id):
    details = Article.objects.get(id = id , author =request.user)
    details.delete()
    return redirect ('user-articles')

