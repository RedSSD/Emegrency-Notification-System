from django.urls import path, include
from .views import UserGroupListAPIView, UserGroupDetailAPIView, NotificationTemplateAPIView

app_name = 'templates'

urlpatterns = [
    path('group/', UserGroupListAPIView.as_view()),
    path('group/<int:id>/', UserGroupDetailAPIView.as_view()),
    #path('group/create/', UserGroupCreateAPIView.as_view()),
    path('template/<int:id>', NotificationTemplateAPIView.as_view()),
]