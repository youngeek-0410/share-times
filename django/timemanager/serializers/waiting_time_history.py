from account.serializers import OrganizationSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model

from ..models import WaitingTimeHistory


class WaitingTimeHistorySnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingTimeHistory
        fields = "__all__"


class WaitingTimeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingTimeHistory
        fields = ("uuid", "waiting_time", "organization", "created_at")

    organization = OrganizationSerializer()


class WaitingTimeHistorySubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingTimeHistory
        fields = ("waiting_time", "organization")

    organization = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        required=True,
    )
