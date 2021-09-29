from core.models import AbstractBaseModelMixin

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


def validate_waiting_time(value):
    MAX_WAITING_TIME = 300
    if not (0 <= value <= MAX_WAITING_TIME):
        raise ValidationError("待ち時間は0分以上かつ" + str(MAX_WAITING_TIME) + "分以下である必要があります")


class WaitingTimeHistory(AbstractBaseModelMixin, models.Model):
    """
    Model for the waiting time history of a exhibition.

    Attributes:
        waiting_time: The waiting time of the exhibition.
        organization: The organization which the waiting time is recorded.
    """

    organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("展示団体"))
    waiting_time = models.PositiveSmallIntegerField(verbose_name=_("待ち時間"), validators=[validate_waiting_time])

    def __str__(self):
        return (
            self.organization.name
            + ":"
            + str(self.waiting_time)
            + "分"
            + "("
            + self.created_at.strftime("%Y/%m/%d %H:%M:%S")
            + ")"
        )

    class Meta:
        verbose_name = _("待ち時間履歴")
        verbose_name_plural = _("待ち時間履歴")
        ordering = ["-created_at"]
