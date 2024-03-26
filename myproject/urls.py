from django.contrib import admin
from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    # for contact links
    # path("contact/", views.contact_view, name="contact"),
    path('success/', views.success_view, name='success'),
]
