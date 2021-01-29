from django.urls import path

from .views import CountdownCreateView, CountdownDetailView

app_name = 'countdown_core'

urlpatterns = [
    path('create/', CountdownCreateView.as_view(), name='create'),
    path('<int:pk>/', CountdownDetailView.as_view(), name='detail')
]
