from django.urls import include, path

from .routers import organization

app_name = "account"

urlpatterns = [
    path("", include(organization.urls)),
]
