from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetCompleteView

from .views import SignUpView, ActivateAccountView, PasswordResetView, PasswordResetConfirmView, UserDeletionView, \
    LoginView, SignupSuccessView

app_name = 'custom_user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='custom_user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-account/', UserDeletionView.as_view(), name='delete_user'),
    path('activate/<uidb64>/<token>', ActivateAccountView.as_view(), name='activate'),

    # password reset views
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-asked/', PasswordResetDoneView.as_view(template_name='custom_user/password_reset_asked.html'),
         name='password_reset_asked'),
    path('set-new-password/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-completed/',
         PasswordResetCompleteView.as_view(template_name='custom_user/password_reset_completed.html'),
         name='password_reset_done'),

    # message views
    path('message/signup-success', SignupSuccessView.as_view(), name='message_signup_success'),
]
