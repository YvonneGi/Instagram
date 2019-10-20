from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Comment,Like,Follow,User
from .forms import NewPostForm,ProfileForm,CommentForm,LikeForm,FollowForm
from django.db.models import Q
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    posts= Post.objects.all().order_by("-id")
    profiles= Profile.objects.all()
    current_user = request.user

    comments=Comment.objects.all()
    likes = Like.objects.all()

    for post in posts:
        num_likes=0
        for like in likes:
            if post.id == like.post.id:
                num_likes +=1
        post.likes = num_likes
        post.save()

    if request.method == 'POST' and 'liker' in request.POST:
        post_id = request.POST.get("liker")
        likeform = LikeForm(request.POST)
        if likeform.is_valid():
            post_id = int(request.POST.get("liker"))
            post = Post.objects.get(id = post_id)
            like = likeform.save(commit=False)
            like.username = request.user
            like.post = post
            like.control = str(like.username.id)+"-"+str(like.post.id)
            like.save()
            print("like saved")

        return redirect("welcome")
    else:
        likeform = LikeForm()

    if request.method == 'POST' and 'unliker' in request.POST:
        post_id = request.POST.get("unliker")
        post = Post.objects.get(pk=post_id)
        control = str(request.user.id)+"-"+str(post.id)
        like_delete = Like.objects.get(control=control)
        like_delete.delete()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST.get("idpost"))
            post = Post.objects.get(id = post_id)
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = post
            comment.save()
        return redirect('welcome')

    else:
        form = CommentForm()

    posts= Post.objects.all().order_by("-id")
    likes = Like.objects.all()
    likez = Like.objects.values_list('control', flat=True)
    likez =list(likez)

    return render(request,'welcome.html',{"posts":posts,"profiles":profiles,"current_user":current_user,"comments":comments,"form":form, "likeform":likeform, "likes":likes,"likez":likez,})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})


@login_required(login_url='/accounts/login/')
def explore(request):
    posts = Post.objects.all()
    profiles= Profile.objects.all()[:3]
    
    return render(request,"explore.html",{"posts":posts,"profiles":profiles,})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    posts = Post.objects.filter(upload_by = user)
    posts = Post.objects.all()
    follows = Follow.objects.all()

    if request.method == 'POST' and 'follower' in request.POST:
        print("follow saved")
        followed_user_id = request.POST.get("follower")
        followform = FollowForm(request.POST)
        if followform.is_valid():
            followed_user_id = int(request.POST.get("follower"))
            current_user = Profile.objects.get(username__id=request.user.id)
            follow = followform.save(commit=False)
            follow.username = request.user
            followed_user = User.objects.get(pk=followed_user_id)
            print(followed_user)
            follow.followed = followed_user
            follow.follow_id = str(follow.username.id)+"-"+str(follow.followed.id)
            follow.save()
            print("follow saved")

        return redirect("profile", user.username.id)
    else:
        followform = FollowForm()

    if request.method == 'POST' and 'unfollower' in request.POST:
        followed_user_id = request.POST.get("unfollower")
        followed_user = User.objects.get(pk=followed_user_id)
        follow_id = str(request.user.id)+"-"+str(followed_user.id)
        follow_delete = Follow.objects.get(follow_id=follow_id)
        follow_delete.delete()



    follows = Follow.objects.all()
    followz = Follow.objects.values_list('follow', flat=True)
    followz =list(followz)
    follower =0
    following = 0
    for follow in followz:
        follow = follow.split("-")
        if follow[0] == str(user.username.id):
            following+=1
        if follow[-1] == str(user.username.id):
            follower+=1


    return render(request, "profile.html", {"current_user":current_user,"posts":posts,"user":user,"user_object":user_object, "follows":follows, "followz":followz,"follower":follower,"following":following})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.upload_by = current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
            
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')


    return render(request,'edit_profile.html',locals())


