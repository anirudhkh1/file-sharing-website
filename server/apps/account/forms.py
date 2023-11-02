from django import forms
from django.contrib.auth.forms import UserCreationForm
from server.apps.account.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "EMAIL ADDRESS"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "PASSWORD"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "CONFIRM PASSWORD"}
        )
