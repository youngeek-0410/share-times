from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from ..models import WaitingTimeHistory
from ..serializers import WaitingTimeHistorySerializer, WaitingTimeHistorySubmitSerializer

Organization = get_user_model()


class WaitingTimeHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows waiting time history to be viewed or edited.
    """

    queryset = WaitingTimeHistory.objects.all()
    serializer_class = WaitingTimeHistorySubmitSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action in ["list"]:
            permission_classes = [AllowAny]
        elif self.action in ["create"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = WaitingTimeHistorySubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
