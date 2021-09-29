from django.contrib import admin

from ..models import WaitingTimeHistory


@admin.register(WaitingTimeHistory)
class WaitingTimeHistoryAdmin(admin.ModelAdmin):
    list_display = ("organization", "waiting_time", "created_at")
    search_fields = ("organization",)
    ordering = ("-created_at",)
    list_filter = ("organization",)
