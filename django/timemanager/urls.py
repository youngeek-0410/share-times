from django.urls import include, path

from .routers import waiting_time_history

app_name = "timemanager"

urlpatterns = [
    path("", include(waiting_time_history.urls)),
]
