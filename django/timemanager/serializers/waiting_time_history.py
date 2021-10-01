from account.serializers import OrganizationSerializer
from rest_framework import serializers


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
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class WaitingTimeHistorySubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingTimeHistory
        fields = ("waiting_time", "organization")

    organization = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
