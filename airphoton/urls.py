from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from airphoton import views

urlpatterns = [
	url(r'^ping/$', views.ping),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'', views.home, name="home"),
]
