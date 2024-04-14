from django.urls import path, include
from .views import UserGroupListAPIView

app_name = 'templates'

urlpatterns = [
    path('group/', UserGroupListAPIView.as_view()),
]