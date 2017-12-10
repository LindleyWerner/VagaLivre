from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^search$', views.search, name='search'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^cadastrarusuario', views.cadastrar_usuario, name='cadastrarusuario'),
]
