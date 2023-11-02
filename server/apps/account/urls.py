from django.urls import path

from server.apps.account import views

app_name = "account"

urlpatterns = [
    path("register", views.RegistrationView.as_view(), name="register"),
]
