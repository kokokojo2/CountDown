from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countdown/', include('countdown_core.urls', namespace='countdown'))
]
