from django.shortcuts import render
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint for users. Can only view / edit yourself!
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Custom permissions. Only admins can view everyone.
        """
        if self.action == 'list':
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [permissions.IsAdminUser, ]

        return super(self.__class__, self).get_permissions()

    # Reference: https://stackoverflow.com/a/58168950/13279459
    @action(detail=False, methods=['get', 'put', 'patch', 'delete'])
    def me(self, request):
        """
        Custom /users/me endpoint.
        """
        self.kwargs['pk'] = request.user.pk

        if request.method == 'GET':
            return self.retrieve(request)
        elif request.method == 'PUT':
            return self.partial_update(request)
        elif request.method == 'PATCH':
            return self.partial_update(request)
        elif request.method == 'DELETE':
            return self.destroy(request)
        else:
            raise Exception('Not implemented')