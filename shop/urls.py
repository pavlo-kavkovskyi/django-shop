from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("terms/", views.terms, name="terms"),
    path("api/info/", views.api_info, name="api_info"),
    path("admin-panel/", views.admin_panel, name="admin_panel"),
]
