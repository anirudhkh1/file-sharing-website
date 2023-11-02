from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView

from server.apps.account.forms import CustomUserCreationForm, UserLoginForm


# Create your views here.
class UserRegistrationView(FormView):
    """Logic to register a new user using email"""

    template_name = "account/registration.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        """Redirect to the home page if already authenticated"""
        if request.user.is_authenticated:
            return redirect(
                reverse_lazy("index"),
            )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Saves the user to DB"""
        user = form.save(commit=False)
        # Additional customizations for the user (if needed)
        user.is_active = False

        # Save the user to the database
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        """Returns the data back to original form with errors"""
        return self.render_to_response(self.get_context_data(form=form))


class UserLoginView(LoginView):
    """CBV login view"""

    form_class = UserLoginForm
    template_name = "account/login.html"
    success_url = reverse_lazy("index")
    redirect_authenticated_user = True


class LogoutView(View):
    """Logout view"""

    def get(self, request):
        """Logouts user and redirects to homepage"""
        logout(request)
        return redirect(reverse_lazy("index"))
