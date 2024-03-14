from rest_framework import serializers
from workervault.models import *


class WorkerVaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerVaultModel
        fields = (
            'userid',
            'name',
            'phoneno',
            'emailid',
            'role',
            'job',
            'address',
            'gender',
            'location',
            'password'
        )
        


        
class AddNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddNews
        fields = (
            'newsid',
            'title',
            'description',
            'image',
            'location',
            'content'
        )
        
        
class AdminAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAdd
        fields = (
            'job_id',
            'job_name'
        )
        
        
        
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class ChatSerializer(serializers.ModelSerializer):
    user = WorkerVaultSerializer(source='name', read_only=True)
    class Meta:
        model = Chat
        fields = '__all__'
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        

class FeedbackSerializer(serializers.ModelSerializer):
    sender = WorkerVaultSerializer(source='sender_name', read_only=True)
    class Meta:
        model = FeedbackModel
        fields = '__all__'