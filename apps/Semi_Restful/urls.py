from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^products$', views.index, name = "index"),
	url(r'^products/new$', views.createDisplay, name = "createDisplay"),
	url(r'^productscreate$', views.create, name = "create"),
	url(r'^products(?P<id>\d+)$', views.show, name = "show"),
	url(r'^products(?P<id>\d+)/editDisplay$', views.editDisplay, name = "editDisplay"),
	url(r'^products(?P<id>\d+)/edit$', views.edit, name = "edit"),
	url(r'^products(?P<id>\d+)/delete$', views.delete, name = "delete")
	# url(r'^(?P<id>\d+)/newcomment$', views.comment)
]