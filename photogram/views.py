from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Comment,Like,Follow,User
from .forms import ProfileForm,CommentForm,LikeForm
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

        return redirect("timeline")
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

