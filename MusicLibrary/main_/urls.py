from django.conf.urls import include, url
from . import views

urlpatterns = [
	# /, /index, /home, /main_ i.e. whatever in <project folder>/urls.py + nothing added "^$" (empty regualr exp)
	url(r'^$', views.index, name='main_index'),
	# /contact, /index/contact, /home/contact, /main_/contact
	url(r'^contact/$', views.contact, name='main_contact'),
]
