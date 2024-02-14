from rest_framework import serializers
from workervault.models import AddNews, AdminAdd, WorkerVaultModel


class WorkerVaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerVaultModel
        fields = (
            'userid',
            'name',
            'phoneno',
            'emailid',
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