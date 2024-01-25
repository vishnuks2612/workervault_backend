from rest_framework import serializers
from workervault.models import WorkerVaultModel


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