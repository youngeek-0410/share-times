from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organizations to be viewed or edited.
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ["list"]:
            permission_classes = (AllowAny,)
        elif self.action in ["create", "destroy"]:
            permission_classes = (IsAdminUser,)
        elif self.action in ["update", "partial_update"]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
