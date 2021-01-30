from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView


app_name = 'custom_user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='custom_user/login.html'), name='login')
]
