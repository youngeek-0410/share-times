import logging

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from ..models import WaitingTimeHistory
from ..serializers import WaitingTimeHistorySerializer, WaitingTimeHistorySubmitSerializer

logging = logging.getLogger(__name__)
Organization = get_user_model()


class WaitingTimeHistoryViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows waiting time history to be viewed or edited.
    """

    queryset = WaitingTimeHistory.objects.all()
    serializer_class = WaitingTimeHistorySubmitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        logging.debug(request.data)
        serializer = WaitingTimeHistorySubmitSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(organization=request.user)
            serializer = WaitingTimeHistorySerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        dict = {}
        if self.request.query_params.get("only-latest") == "true":
            for org in Organization.objects.filter(is_admin=False):
                queryset = (
                    WaitingTimeHistory.objects.filter(organization__uuid=org.uuid).order_by("-created_at").first()
                )
                dict[org.name] = WaitingTimeHistorySerializer(queryset).data
        else:
            for org in Organization.objects.filter(is_admin=False):
                queryset = WaitingTimeHistory.objects.filter(organization__uuid=org.uuid).order_by("-created_at")
                dict[org.name] = WaitingTimeHistorySerializer(queryset, many=True).data
        return Response(dict, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = WaitingTimeHistorySerializer(instance)
        return Response(serializer.data)
