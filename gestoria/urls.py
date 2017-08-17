from django.conf.urls import url
from . import views
from gestoria.views import llistat

urlpatterns = [
	url(r'^$', views.news, name='news'),
	url(r'^news/', views.news, name='news'),
	url(r'^llistat', llistat.as_view(), name='llistat'),
	url(r'^map/', views.map, name='map'),
	url(r'^resposta/', views.resposta, name='resposta'),
	url(r'^contacte/', views.contacte, name='contacte'),
]