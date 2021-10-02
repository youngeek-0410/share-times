import logging

from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Organization
from .serializers import OrganizationSerializer, OrganizationUpdateFromUserSerializer

logger = logging.getLogger(__name__)


class OrganizationViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows organizations to be viewed or edited.
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationUpdateFromUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset = Organization.objects.filter(is_admin=False)
        serializer = OrganizationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        if request.user.uuid != instance.uuid and not request.user.is_admin:
            raise PermissionDenied("You are not allowed to submit this data.")
        serializer = OrganizationSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrganizationSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
