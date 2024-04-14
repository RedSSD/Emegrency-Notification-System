from rest_framework import serializers
from .models import UserGroup, Template


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
