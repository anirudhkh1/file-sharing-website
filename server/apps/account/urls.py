from django.urls import path

from server.apps.account import views

app_name = "account"

urlpatterns = [
    path("register", views.UserRegistrationView.as_view(), name="register"),
    path("login", views.UserLoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
