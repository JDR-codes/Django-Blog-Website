from django.shortcuts import redirect, render
from .models import *
from . forms import *
from articles.models import *
# Create your views here.


def user_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            Profile.objects.create(user = request.user, **form.cleaned_data)
            return redirect ('articles-list')
    
    form = ProfileForm()
    return render (request,'user_create.html',{'form' : form})

# to view a particular user profile (similar to insta:no of blog posts/articles, total number of likes overall, user bio, picture, list all the blogs posted)
def view_profile(request,user):
    context = {}

    user = User.objects.get(username = user)
    profile = Profile.objects.get(user = user)
    articles = Article.objects.filter(author = user)
    no_of_posts = len(articles)

    following = 0
    for follow in profile.following.all():
        following += 1

    followers = 0
    for follow in profile.followers.all():
        followers += 1

    context['profile'] = profile
    context['articles'] = articles
    context['no_of_posts'] = no_of_posts
    context['following'] = following
    context['followers'] = followers

    return render(request,'profile.html',context)

# user should be able to edit only his own profile, not other users profile
# can edit bio and profile picture only
def edit_profile(request,id):
    pro_det = Profile.objects.get(id=id)
    if request.method == "POST":
        pro_det = Profile.objects.filter(id = id)
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            pro_det.update(user = request.user,**form.cleaned_data)
            return redirect('articles-list')

    
    form = ProfileForm(initial={
        'profile' : pro_det.profile,
        'bio' : pro_det.bio,
        'phone_number' : pro_det.phone_number,
    })

    return render(request,'update_profile.html',{'form' : form})


def follow_user_view(request,id):
    if request.method == 'POST':
        follow = Profile.objects.get(id = id)
        profile = Profile.objects.get(user = request.user)
        if follow.user in profile.following.all():
            profile.following.remove(follow.user)
            follow.followers.remove(profile.user)
        else:
            if profile.user != follow.user:
                profile.following.add(follow.user)
                follow.followers.add(profile.user)


        profile.save()
    return redirect('articles-list')


