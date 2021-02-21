from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm, BootstrapAuthForm, BootstrapPasswordResetForm, BootstrapPasswordSetForm
from .services.user_management_services import process_signup_form, confirm_user_email


class LoginRequiredView(LoginRequiredMixin, View):
    login_url = reverse_lazy('custom_user:login')


# TODO: redirect to dashboard if user is already registered
class SignUpView(View):
    """
    Handles an account creation.
    """
    template_name = 'custom_user/signup.html'

    def post(self, request):
        registration_form = RegistrationForm(request.POST)
        user = process_signup_form(request, registration_form)

        # TODO: implement redirect to a success url with e-mail confirmation message
        if user:
            return HttpResponse('The user was successfully created.')

        return render(request, self.template_name, {'form': registration_form})

    def get(self, request):
        return render(request, self.template_name, {'form': RegistrationForm()})


class ActivateAccountView(View):
    """
    This view handles e-mail verification (account confirmation) process.
    After verification is done user loges in the user automatically.
    """
    template_name = 'custom_user/e-mail_confirmation.html'

    def get(self, request, uidb64, token):
        user = confirm_user_email(uidb64, token)
        login(request, user)
        # TODO: make a redirect to a dashboard if the email is confirmed, and render a template if smth goes wrong
        return render(request, self.template_name, {'confirmed': True if user else False})


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'custom_user/password_reset.html'
    email_template_name = 'email/password_reset.html'
    success_url = reverse_lazy('custom_user:password_reset_asked')
    form_class = BootstrapPasswordResetForm


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'custom_user/password_reset_confirm.html'
    success_url = reverse_lazy('custom_user:password_reset_done')
    form_class = BootstrapPasswordSetForm


class UserDeletionView(LoginRequiredView):
    """
    This view handles account deletion.
    """
    template_name = 'custom_user/delete_account.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        request.user.delete()

# message pages views
class SignupSuccessView(View):

    def get(self, request):
        return render(request, template_name='custom_user/signup_successful.html')
