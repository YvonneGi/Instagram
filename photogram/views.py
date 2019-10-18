from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from .forms import ProfileForm,ImageForm
from .models import Profile,Post,Comment,Like,Follow,User
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# from friendship.exceptions import AlreadyExistsError
from django.db.models import Q
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  date = dt.date.today()
  posts= Post.objects.all().order_by("-id")
  profiles= Profile.objects.all()
  current_user = request.user
  return render(request,'welcome.html',{"date": date,"posts": posts,"profiles": profiles,"current_user": current_user})

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

@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'image.html',locals())

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)
    usersss = User.objects.get(id=id)
    follower = len(Follow.objects.followers(usersss))
    following = len(Follow.objects.following(usersss))
    people=User.objects.all()
    pip_following=Follow.objects.following(request.user)

    return render(request,'profile/profile.html',locals())
                
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