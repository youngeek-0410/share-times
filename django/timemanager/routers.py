from rest_framework import routers

from .views import WaitingTimeHistoryViewSet

waiting_time_history = routers.DefaultRouter()
waiting_time_history.register(r"waiting_time_history", WaitingTimeHistoryViewSet)
