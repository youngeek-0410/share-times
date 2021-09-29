from rest_framework import serializers

from .models import Organization


class OrganizationSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("uuid", "name", "description")
