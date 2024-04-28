from django.contrib import admin
from .models import UserGroup, NotificationTemplate

# Register your models here.
admin.site.register(UserGroup)
admin.site.register(NotificationTemplate)
