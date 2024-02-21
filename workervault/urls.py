from django.urls import path, include
from .import views
from .views import MessageAPIView


urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('login/', views.loginView, name="login"),
    path('userview/', views.userView, name="userview"),
    path('addnews/', views.addnewsView, name="addnews"),
    path('viewnearnews/', views.viewnearNews, name='viewnearnews'),
    path('addservicesview/', views.addservicesView, name='addservicesview'),
    path('viewservicelist/', views.viewservicelistView, name="viewservicelist"),
    path('contactus/', views.contactUs, name="contactus"),
    
    
    path('messages/', MessageAPIView.as_view())
]
