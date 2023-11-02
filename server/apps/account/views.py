from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from server.apps.account.forms import CustomUserCreationForm
from server.apps.account.models import User


# Create your views here.
class RegistrationView(FormView):
    template_name = "account/registration.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save(commit=False)
        # Additional customizations for the user (if needed)
        user.is_active = False

        # Save the user to the database
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
