from rest_framework import serializers
from .models import UserGroup, NotificationTemplate


class NotificationTemplateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = (
            'pk',
            'name'
        )


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = '__all__'


class UserGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('pk', 'name')


class UserGroupSerializer(serializers.ModelSerializer):
    group_templates = NotificationTemplateListSerializer(many=True)

    class Meta:
        model = UserGroup
        fields = (
            'pk',
            'name',
            'receivers',
            'group_templates',
            'owner'
        )
