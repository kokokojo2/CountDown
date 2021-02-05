from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .tokens import EmailConfirmationTokenGenerator
from .models import CustomUser


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

        # TODO: implement redirect to a success url with e-mail confirmation message
        if registration_form.is_valid():
            user = registration_form.save()

            token_generator = EmailConfirmationTokenGenerator()

            email_body = render_to_string('email/user_confirmation.html', {
                'user': user,
                'raw_password': registration_form.cleaned_data['password1'],
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token_generator.make_token(user),
                'domain': get_current_site(request).domain
            })

            send_mail('Activate your account.', email_body, 'countdownapp@app.com', [user.email], fail_silently=False)
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
        token_generator = EmailConfirmationTokenGenerator()
        confirmed = False

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
            # TODO: add a logging here

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)

            confirmed = True

        # TODO: make a redirect to a dashboard if the email is confirmed, and render a template if smth goes wrong
        return render(request, self.template_name, {'confirmed': confirmed})


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'custom_user/password_reset.html'
    email_template_name = 'email/password_reset.html'
    success_url = reverse_lazy('custom_user:password_reset_asked')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'custom_user/password_reset_confirm.html'
    success_url = reverse_lazy('custom_user:password_reset_done')


class UserDeletionView(LoginRequiredView):
    """
    This view handles account deletion.
    """

    template_name = 'custom_user/delete_account.html'

    def get(self, request):
        print(request.user.is_authenticated)
        return render(request, self.template_name)

    def post(self, request):
        user = request.user
        user.delete()

        # TODO: redirect to smth or make real template
        return HttpResponse('Your account was successfully deleted.')
