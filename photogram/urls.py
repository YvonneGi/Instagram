from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import RedirectView

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url(r'^search/', views.search_user, name='search_user'),
    # url(r'^explore/', views.explore, name = 'explore'),
    # url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    # url(r'^new/post/', views.new_post, name = 'new-post'),
    # url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    # url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico'))

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)