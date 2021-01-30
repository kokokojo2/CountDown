from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('countdown/', include('countdown_core.urls', namespace='countdown')),
    path('', include('custom_user.urls', namespace='users')),
]



