import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class OrganizationManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, password):
        if not name:
            raise ValueError("The given name must be set")
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.model(name=name)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Organization(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(
        _("name"),
        max_length=250,
        unique=True,
    )
    MAX_LENGTH_DESCRIPTION = 400
    description = models.CharField(
        verbose_name=_("展示概要"),
        blank=True,
        max_length=MAX_LENGTH_DESCRIPTION,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = OrganizationManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")
