from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^new/post/$', views.new_post, name='new-post'),
    url(r'^new/profile/$', views.new_profile, name='new-profile'),
    # url(r'^profile/$', views.profile, name='profile'),
    
]
