from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsGroupOwnerPermission, IsNotificationTemplateOwnerPermission

from .models import UserGroup, NotificationTemplate
from .serializers import UserGroupListSerializer, UserGroupSerializer, NotificationTemplateSerializer


class UserGroupListAPIView(ListAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = UserGroupListSerializer

    def get_queryset(self):
        return UserGroup.objects.filter(owner=self.request.user)


class UserGroupDetailAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, IsGroupOwnerPermission)
    serializer_class = UserGroupSerializer

    def get_object(self):
        obj = get_object_or_404(UserGroup, pk=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)
        return obj


"""class UserGroupCreateAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = UserGroupSerializer

    def current_user(self):
        return (
            self.request.user if self.request.user.is_authenticated else None
        )

    def _profile(self):
        return get_object_or_404(
            UserGroup.objects.active_only(),
            pk=self.kwargs['id']
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.current_user())
        """


class NotificationTemplateAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, IsNotificationTemplateOwnerPermission)
    serializer_class = NotificationTemplateSerializer

    def get_object(self):
        obj = get_object_or_404(NotificationTemplate, pk=self.kwargs['id'])
        print(obj)
        self.check_object_permissions(self.request, obj)
        return obj
