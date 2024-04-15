from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# Url importing url from other application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myproject.urls'), name='myproject_urls'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico')))
]