from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register")
]