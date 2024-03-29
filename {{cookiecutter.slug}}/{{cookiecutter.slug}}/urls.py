"""
{{cookiecutter.project}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.views.generic import TemplateView


def ping(*args):
    return JsonResponse({"ping": "pong"})


urlpatterns = [
    # Ping test endpoint
    path("ping/", ping, name="ping"),
    # Django admin
    path("admindocs/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    # {{cookiecutter.project}}
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("", include("{{cookiecutter.slug}}.members.auth.urls")),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("members/", include("{{cookiecutter.slug}}.members.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.views.defaults import (
        bad_request,
        page_not_found,
        permission_denied,
        server_error,
    )

    urlpatterns = [
        # Debug error webpages
        path("400/", bad_request, kwargs={"exception": Exception("Bad Request")}),
        path("403/", permission_denied, kwargs={"exception": Exception("Forbidden")}),
        path("404/", page_not_found, kwargs={"exception": Exception("Not Found")}),
        path("500/", server_error),
    ] + urlpatterns

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
