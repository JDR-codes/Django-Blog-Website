from django.shortcuts import redirect, render
from articles.models import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

# ------------ COMMENTS ------------ #
# add a comment to a particular post
@login_required(login_url='login')
def add_comment_view(request, id):
    context = {}
    if request.method == 'POST':
        Comment.objects.create(
            post = Article.objects.get(id = id),
            user = request.user,
            comment = request.POST.get('comment','')
        )
        return redirect ('add-comment',id)
    
    comments = Comment.objects.filter(post = id)
    if comments:
        context['comments'] = comments
    else:
        context['msg'] = 'No Comments '
    return render(request,'comment.html',context)

def delete_comment_view(request, id):
    comment = Comment.objects.get(id = id)
    post = comment.post
    comment.delete()
    return redirect('article-details',post.id)


# ------------ LIKES ------------ #
def like_article_view(request,id):
    if request.method == 'POST':
        article = Article.objects.get(id = id)
        try: 
            like = Like.objects.get(post = article)
        except:
            Like.objects.create(post = article)
            like = Like.objects.get(post = article)
        
        if request.user in like.user.all() :
            like.like_count -= 1
            like.user.remove(request.user)
        else:
            like.user.add(request.user)
            like.like_count += 1
        like.save()
        
        return redirect ('article-details',id)

    