"""crwdbtcsboard_38334 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("modules/", include("modules.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("api/v1/", include("users.api.v1.urls")),

    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("api/v1/", include("apps.api.v1.urls")),
    path("apps/", include("apps.urls")),
    path("api/v1/", include("plans.api.v1.urls")),
    path("plans/", include("plans.urls")),
    path("api/v1/", include("subscriptions.api.v1.urls")),
    path("subscriptions/", include("subscriptions.urls")),











]

admin.site.site_header = "crwdbtcsboard"
admin.site.site_title = "crwdbtcsboard Admin Portal"
admin.site.index_title = "crwdbtcsboard Admin"

# swagger
urlpatterns += [
    path("api-docs/schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path("api-docs/", SpectacularSwaggerView.as_view(url_name='schema'), name="api_docs")
]

