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
    path("hello/<str:name>/", views.hello, name="hello"),
    path("hello/<str:name>/<int:age>/", views.hello_age, name="hello_age"),
    path("add/<int:a>/<int:b>/", views.add, name="add"),
    path("subtract/<int:a>/<int:b>/", views.subtract, name="subtract"),
    path("multiply/<int:a>/<int:b>/", views.multiply, name="multiply"),
    path("divide/<int:a>/<int:b>/", views.divide, name="divide"),
]
