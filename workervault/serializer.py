from rest_framework import serializers
from workervault.models import AddNews, AdminAdd, ContactUs,  WorkerVaultModel


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
        fields = (
            'userid',
            'description'
        )