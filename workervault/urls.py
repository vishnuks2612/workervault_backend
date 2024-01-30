from django.urls import path, include
from .import views
urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('login/', views.loginView, name="login"),
    path('userview/', views.userView, name="userview"),
    path('addnews/', views.addnewsView, name="addnews"),
    path('viewnearnews/', views.viewnearNews, name="viewnearnews"),
]
