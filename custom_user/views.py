from django.shortcuts import render, redirect
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


class LoginView(auth_views.LoginView):
    authentication_form = BootstrapAuthForm
    redirect_authenticated_user = True
    red = reverse_lazy('countdown:dashboard')


class SignUpView(View):
    """
    Handles an account creation.
    """
    template_name = 'custom_user/signup.html'

    def post(self, request):
        registration_form = RegistrationForm(request.POST)
        user = process_signup_form(request, registration_form)

        if user:
            return redirect(reverse_lazy('custom_user:message_signup_success'))

        return render(request, self.template_name, {'form': registration_form})

    def get(self, request):

        if request.user.is_anonymous:
            print(request.user)
            return render(request, self.template_name, {'form': RegistrationForm()})

        return redirect('countdown:dashboard')


class ActivateAccountView(View):
    """
    This view handles e-mail verification (account confirmation) process.
    After verification is done user loges in the user automatically.
    """
    template_name = 'custom_user/e-mail_confirmation.html'

    def get(self, request, uidb64, token):
        user = confirm_user_email(uidb64, token)
        if user is not None:
            login(request, user)
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
        return redirect('home')


# message pages views
class SignupSuccessView(View):

    def get(self, request):
        return render(request, template_name='custom_user/signup_successful.html')
