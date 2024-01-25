import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from workervault.serializer import WorkerVaultSerializer

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