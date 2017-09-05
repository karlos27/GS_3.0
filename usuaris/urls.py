from django.conf.urls import url
from . import views
from usuaris.views import RegistreUsuari, descarregues


urlpatterns = [
	url(r'^registre/', RegistreUsuari.as_view(), name='registre'),
	url(r'^perfil/', views.Perfil, name='perfil'),
	url(r'^inici/', views.inici, name='inici'),
	url(r'^registre_up/', views.registre_up, name='registre_up'),
	url(r'^descarregues/', descarregues.as_view(), name='descarregues'),
	]