from django.contrib.auth.backends import ModelBackend

from .models import CustomUser


class CustomUserAuthBackend(ModelBackend):
    """
    Custom backend used for user authentication by email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password) is True:
                return user

        except CustomUser.DoesNotExist:
            return None
