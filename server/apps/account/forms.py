from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from server.apps.account.models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form inherited from user creation form"""

    class Meta(UserCreationForm.Meta):
        """Added fields to use only 3 fields and not username"""

        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        """To add form classes"""
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "EMAIL ADDRESS"},
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "PASSWORD"},
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "CONFIRM PASSWORD"},
        )


class UserLoginForm(AuthenticationForm):
    """User login form inherited from Authentication Form"""

    username = forms.EmailField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "EMAIL ADDRESS"},
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "PASSWORD"},
        ),
    )
