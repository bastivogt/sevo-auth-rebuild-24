"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from sevo_auth.views import fake_home

from sevo_pages.views import homepage

from sevo_maintainance.views import maintainance





urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("sevo_auth.urls")),
    path("", homepage, name="homepage"),
    path("page/", include("sevo_pages.urls")),

    path("immo/", include("immo_test.urls")),
    path("page/", include("sevo_pages.urls")),
    path("maintainance/", maintainance, name="sevo-maintainance")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
