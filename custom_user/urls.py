from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView


app_name = 'custom_user'

# TODO: change a logout template when it`s ready
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='custom_user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='custom_user/logout.html'), name='logout'),
]

