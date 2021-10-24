"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework.authtoken.views as auth_views

from django.contrib import admin
from django.urls import include, path

admin.site.site_title = "share-times"  # URL title
admin.site.site_header = "展示待ち時間管理システム"  # title
admin.site.index_title = "share-times"  # sub title

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", auth_views.obtain_auth_token),
    path("api/", include("timemanager.urls")),
    path("api/", include("account.urls")),
]
