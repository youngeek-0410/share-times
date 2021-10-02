from account.organization_type import OrganizationType
from rest_framework import serializers

from .models import Organization


class OrganizationSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("uuid", "name", "description", "type")

    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return OrganizationType.name_of_value(obj.type)


class OrganizationUpdateFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("description",)
