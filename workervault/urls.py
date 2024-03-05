from django.urls import path, include
from .import views


urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('login/', views.loginView, name="login"),
    path('userview/', views.userView, name="userview"),
    path('addnews/', views.addnewsView, name="addnews"),
    path('viewnearnews/', views.viewnearNews, name='viewnearnews'),
    path('addservicesview/', views.addservicesView, name='addservicesview'),
    path('viewservicelist/', views.viewservicelistView, name="viewservicelist"),
    path('contactus/', views.contactUs, name="contactus"),
    path('viewQueries/', views.viewQueries, name="viewQueries"),
    path('findWorkers/', views.findWorkers, name="findWorkers"),
    path('AddJob/', views.AddJob, name="AddJob"),
    path('saveChat/', views.user_chat_view, name="saveChat"),
    path('viewChat/', views.view_user_chat_view, name="viewChat"),
    # path('recievedChat/', views.recieved_chat_view, name="recievedChat"),
    path('adminLogin/', views.adminLogin, name="adminLogin"),
    path('viewProfile/', views.view_profile_view, name="viewProfile"),
    path('EditProfile/', views.EditProfile, name="EditProfile"),
    path('savefeedback/', views.feedback, name="savefeedback"),
    path('viewFeedback/', views.viewFeedback, name="viewFeedback"),
    path('deleteView/', views.deleteView, name="deleteView"),
    
    
    
]
