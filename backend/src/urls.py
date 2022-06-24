from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    # index(home) url must be end of the urls and it will catch all urls by re_path regular expression
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html"), name="home"),
]
