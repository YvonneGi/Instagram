from django.http  import HttpResponse
from django.shortcuts import render
# import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})