from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile,Post,Comment,Like,Follow,User
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  date = dt.date.today()
  posts= Post.objects.all().order_by("-id")
  profiles= Profile.objects.all()
  current_user = request.user
  comments = Comment.objects.all()
  likes = Like.objects.all()
  return render(request,'welcome.html',{"date": date,"posts":posts,"profiles":profiles,"current_user":current_user,
                "comments":comments,"likes":likes})

@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/new.html', locals())
                
@login_required(login_url='/accounts/login/')
def search_user(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})