from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .forms import RegistrationForm


# TODO: redirect to dashboard if user is already registered
class SignUpView(View):
    """
    Handles an account creation.
    """

    template_name = 'custom_user/signup.html'

    def post(self, request):
        registration_form = RegistrationForm(request.POST)

        # TODO: implement redirect to a success url with e-mail confirmation message
        if registration_form.is_valid():
            registration_form.save()

            return HttpResponse('The user was successfully created.')

        return render(request, self.template_name, {'form': registration_form})

    def get(self, request):
        return render(request, self.template_name, {'form': RegistrationForm()})
