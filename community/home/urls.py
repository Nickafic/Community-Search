from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add,name = 'add'),
    path('logout', views.logout_view, name = 'logout'),
    path('login', views.loginPage, name = 'login'),
    path('create', views.create, name = 'create'),
    path('mygroups', views.mygroups, name = 'mygroups'),
    path('results', views.results, name = 'results'),
]

