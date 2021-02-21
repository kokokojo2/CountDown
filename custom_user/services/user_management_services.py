from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

from ..models import CustomUser
from ..tokens import EmailConfirmationTokenGenerator


def process_signup_form(request, form):
    """
    Handles form validation and sending confirmation email. Raises an exception if email service crashes.
    :return: user object - form is valid, None - form is invalid
    """

    if form.is_valid():
        user = form.save()

        token_generator = EmailConfirmationTokenGenerator()

        email_body = render_to_string('email/user_confirmation.html', {
            'user': user,
            'raw_password': form.cleaned_data['password1'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user),
            'domain': get_current_site(request).domain
        })
        send_mail('Activate your account.', email_body, 'countdownapp@app.com', [user.email], fail_silently=False)

        return user


def confirm_user_email(uidb64, token):
    """
    Handles user confirmation process.
    :param uidb64: uid in base64 encoding from url
    :param token: confirmation token for EmailConfirmationTokenGenerator from url
    :return: user object if user is confirmed, None - user is not confirmed
    """

    token_generator = EmailConfirmationTokenGenerator()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
        # TODO: add a logging here

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
    else:
        return None

    return user
