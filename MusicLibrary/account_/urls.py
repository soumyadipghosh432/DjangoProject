from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='account_login'),
	url(r'^doLogin/$', views.doLogin, name='account_doLogin'),
	url(r'^register/$', views.register, name='account_register'),
	url(r'^doRegister/$', views.doRegister, name='account_doRegister'),
	url(r'^homepage/$', views.homepage, name='account_homepage'),
]