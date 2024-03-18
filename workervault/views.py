import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from workervault.models import *
from workervault.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .pusher import pusher_client
from rest_framework.decorators import api_view


# Create your views here.

@csrf_exempt
def registerView(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        serializer_check = WorkerVaultSerializer(data=received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        



@csrf_exempt
def loginView(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        getEmailId = received_data['emailid']
        getPassword = received_data['password']
        loginData = WorkerVaultModel.objects.filter(Q(emailid__exact = getEmailId) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    else:
        return HttpResponse(json.dumps("Failed"))
    
    
@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        getUsername = received_data['username']
        getPass = received_data['password']
        loginData = Admin.objects.filter(Q(username__exact = getUsername              ) & Q(password__exact = getPass)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    else:
        return HttpResponse(json.dumps("Failed"))
    
    

  
        
@csrf_exempt
def addnewsView(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        serializer_check = AddNewsSerializer(data=received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
        

@csrf_exempt
def addservicesView(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        serializer_check = AdminAddSerializer(data = received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
 

@csrf_exempt
def contactUs(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = ContactUsSerializer(data = received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        



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
def viewQueries(request):
    if request.method == 'POST':
        queries = ContactUs.objects.all()
        serialize_data = ContactUsSerializer(queries, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))    
    
    
@csrf_exempt
def viewservicelistView(request):
    if request.method == 'POST':
        viewlist = AdminAdd.objects.all()
        serialize_data = AdminAddSerializer(viewlist, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))
    
    
    
    
@csrf_exempt
def findWorkers(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        getWorker = received_data["job"]
        data = WorkerVaultModel.objects.filter(Q(job__icontains=getWorker)).all()
        serializer_data = WorkerVaultSerializer(data, many = True)
        return HttpResponse(json.dumps(serializer_data.data))
    
    
    
    
@csrf_exempt
def AddJob(request):
    if request.method == "PUT":      
        received_data = json.loads(request.body)
        getUserid = received_data["userid"]
        getJob = received_data["job"]
        data = WorkerVaultModel.objects.filter(Q(userid__exact=getUserid))
        data.update(job=getJob)
        return HttpResponse(json.dumps({"status":"Job Added"}))
 
@csrf_exempt
def view_profile_view(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        getUserid = received_data["userid"]
        userList = WorkerVaultModel.objects.filter(Q(userid__exact=getUserid)).all()
        serialize_data = WorkerVaultSerializer(userList, many = True)
        return HttpResponse(json.dumps(serialize_data.data))   
    
@csrf_exempt
def EditProfile(request):
    if request.method == "PUT":
        received_data = json.loads(request.body)
        getUserid = received_data['userid']
        getName = received_data['name']
        getEmail = received_data['emailid']
        getPhone = received_data['phoneno']
        getJob = received_data['job']
        getAddress = received_data['address']
        getLocation = received_data['location']
        data = WorkerVaultModel.objects.filter(Q(userid__exact = getUserid))
        data.update(name = getName, emailid = getEmail, phoneno = getPhone, job = getJob, address = getAddress, location = getLocation)
        return HttpResponse(json.dumps({"status":"Profile Updated"}))
    
    
@csrf_exempt
def submit_chat_view(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        # print(received_data)
        serializer_check = ChatSerializer(data=received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
@csrf_exempt
def get_chat_messages(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        sender_id = received_data.get("name", "")
        receiver_id = received_data.get("receiver_name", "")
        
        # Fetch messages where the sender is the current user and the receiver is the specified recipient
        sender_messages = Chat.objects.filter(Q(sender__exact=sender_id) & Q(receiver__exact=receiver_id))
        
        # Fetch messages where the sender is the specified recipient and the receiver is the current user
        receiver_messages = Chat.objects.filter(Q(sender__exact=receiver_id) & Q(receiver__exact=sender_id))
        
        # Combine both sets of messages
        all_messages = list(sender_messages) + list(receiver_messages)
        
        # Sort the combined messages based on the timestamp in descending order
        sorted_messages = sorted(all_messages, key=lambda x: x.timestamp, reverse=False)
        
        # Serialize the sorted messages
        sorted_messages_data = ChatSerializer(sorted_messages, many=True).data
        
        return JsonResponse(sorted_messages_data, safe=False)

    
@csrf_exempt
def get_employer_details_view(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        get_receiver_name = received_data.get("receiver_name", "")
        
        # Filter Chat objects to get distinct sender names and IDs
        data = Chat.objects.filter(receiver__exact=get_receiver_name).values("sender__name", "sender__userid").distinct()
        
        # Extract sender names and IDs
        unique_senders = [{"userid": item["sender__userid"], "name": item["sender__name"]} for item in data]
        
        return JsonResponse(unique_senders, safe=False)
    
# @csrf_exempt
# def get_employer_chat_view(request):
#     if request.method=='POST':
#         received_data = json.loads(request.body)
#         get_receiver_id=received_data["name"]
#         get_sender_id=received_data["receiver_name"]
#         data = Chat.objects.filter(Q(sender__exact=get_sender_id)&Q(receiver__exact=get_receiver_id)).all()
#         serializer_data = ChatSerializer(data, many = True)
#         return HttpResponse(json.dumps(serializer_data.data))
    
    

@csrf_exempt
def feedback(request):
    if request.method=='POST':
        received_data = json.loads(request.body)
        serializer_check = FeedbackSerializer(data=received_data)
        print(serializer_check)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Feedback Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))
        
        
        
@csrf_exempt
def viewFeedback(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        getRecieverid=received_data["reciever_name"]
        data = FeedbackModel.objects.filter(Q(reciever_name__exact=getRecieverid)).all()
        serialize_data = FeedbackSerializer(data, many = True)
        print(serialize_data)
        return HttpResponse(json.dumps(serialize_data.data))  
    
    
@csrf_exempt
def deleteView(request):
    if request.method == "DELETE":
        recieved_id = request.GET.get('id') 
        getId = (int(recieved_id))
        print(getId)
        if getId is not None:
            try:
                data = AdminAdd.objects.filter(Q(job_id__exact=getId)) 
            except AdminAdd.DoesNotExist:
                return HttpResponse(json.dumps({"status":"Post not Found"}))  
            data.delete()
            return HttpResponse(json.dumps({"status":"Deleted Successfully"}))  
        
        

    
        
        
# @csrf_exempt
# def recieved_chat_view(request):
#     if request.method=='POST':
#         received_data = json.loads(request.body)
#         getRecieverid=received_data["reciever_name"]
#         get_sender_id=received_data["name"]
#         data = MessageModel.objects.filter(Q(reciever_name__exact=getRecieverid)&Q(name__exact=get_sender_id)).all()
#         serializer_data = MessagesSerializer(data, many = True)
#         return HttpResponse(json.dumps(serializer_data.data))
    
    
    
# class MessageAPIView(APIView):
    
#     def post(self, request):
#         pusher_client.trigger('workervault', 'message', {
#             'name': request.data['name'],
#             'message': request.data['message'],
#         })
        
#         return Response([])



@csrf_exempt
@api_view(['POST'])
def send_message(request):
    try:
        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')
        job_id=request.data.get('job_id')

        print(f"Sender ID: {sender_id}, Receiver ID: {receiver_id} , Job ID: {job_id}")

        data = {
            'sender': sender_id,
            'receiver': receiver_id,
            'text': request.data.get('text'),
            'job_id':job_id
            # Include any other fields from your serializer
        }

        # If a file is included in the request, save it to the 'file' field
        file = request.data.get('file')
        if file:
            data['file'] = file

        serializer = ChatSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        print(f"Serializer Errors: {serializer.errors}")
        return JsonResponse(serializer.errors, status=400)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)
    

# @require_GET
@csrf_exempt
def get_user_messages(request, user_id, job_id, emp_id):
    try:
        # Fetch messages where user_id is the receiver
        messages = Chat.objects.filter(receiver=emp_id, job_id=job_id, sender=user_id).order_by('timestamp')
        serializer = ChatSerializer(messages, many=True)
        
        # Serialize file URL to be included in the response
        data = serializer.data
        for message in data:
            if message['file']:
                message['file'] = request.build_absolute_uri(message['file'])

        return JsonResponse(data, safe=False)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)


# @require_GET
@csrf_exempt
def get_emp_messages(request, user_id, job_id, emp_id):
    try:
        # Fetch messages where user_id is the receiver
        messages = Chat.objects.filter(receiver=user_id, job_id=job_id, sender=emp_id).order_by('timestamp')
        serializer = ChatSerializer(messages, many=True)
        
        # Serialize file URL to be included in the response
        data = serializer.data
        for message in data:
            if message['file']:
                message['file'] = request.build_absolute_uri(message['file'])

        return JsonResponse(data, safe=False)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)