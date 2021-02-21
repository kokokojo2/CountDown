from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from home.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countdown/', include('countdown_core.urls', namespace='countdown')),
    path('', HomePageView.as_view(), name='home'),
    path('', include('custom_user.urls', namespace='users')),
]



