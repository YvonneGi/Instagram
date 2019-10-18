from django.http  import HttpResponse
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
  date = dt.date.today()
  if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print('valid')
  else:
        form = ProfileForm()
  return render(request,'welcome.html',{"date": date,"ProfileForm":form})

def search_user(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})