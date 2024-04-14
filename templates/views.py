from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import UserGroup, Template
from .serializers import UserGroupSerializer


class UserGroupListAPIView(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserGroupSerializer

    def get_queryset(self):
        return UserGroup.objects.filter(owner=self.request.user)