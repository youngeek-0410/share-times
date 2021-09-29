from rest_framework import routers

from .views import OrganizationViewSet

organization = routers.DefaultRouter()
organization.register(r"organization", OrganizationViewSet)
