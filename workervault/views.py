import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from workervault.models import AddNews, AdminAdd, WorkerVaultModel
from workervault.serializer import AddNewsSerializer, AdminAddSerializer, ContactUsSerializer, WorkerVaultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .pusher import pusher_client


# Create your views here.

@csrf_exempt
def registerView(request):
    if request.method=='POST':
        recieved_data = json.loads(request.body)
        serializer_check = WorkerVaultSerializer(data=recieved_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
        
        
@csrf_exempt
def addnewsView(request):
    if request.method=='POST':
        recieved_data = json.loads(request.body)
        serializer_check = AddNewsSerializer(data=recieved_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
        

@csrf_exempt
def addservicesView(request):
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        serializer_check = AdminAddSerializer(data = recieved_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
        

@csrf_exempt
def contactUs(request):
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        serializer_check = ContactUsSerializer(data = recieved_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        

@csrf_exempt
def loginView(request):
    if request.method=='POST':
        recieved_data = json.loads(request.body)
        getEmailId = recieved_data['emailid']
        getPassword = recieved_data['password']
        loginData = WorkerVaultModel.objects.filter(Q(emailid__exact = getEmailId) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    else:
        return HttpResponse(json.dumps("Failed"))




@csrf_exempt
def userView(request):
    if request.method=='POST':
        userList = WorkerVaultModel.objects.all()
        serialize_data = WorkerVaultSerializer(userList, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))
    
    
    
@csrf_exempt
def viewnearNews(request):
    if request.method=='POST':
        news = AddNews.objects.all()
        serialize_data = AddNewsSerializer(news, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))
    
    
    
@csrf_exempt
def viewservicelistView(request):
    if request.method == 'POST':
        viewlist = AdminAdd.objects.all()
        serialize_data = AdminAddSerializer(viewlist, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))
    
    
    
    
# class MessageAPIView(APIView):
    
#     def post(self, request):
#         pusher_client.trigger('workervault', 'message', {
#             'name': request.data['name'],
#             'message': request.data['message'],
#         })
        
#         return Response([])