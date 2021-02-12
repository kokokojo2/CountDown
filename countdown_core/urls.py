from django.urls import path

from .views import CountdownCreateView, CountdownDetailView, DashBoardView

app_name = 'countdown_core'

urlpatterns = [
    path('create/', CountdownCreateView.as_view(), name='create'),
    path('<int:pk>/', CountdownDetailView.as_view(), name='detail'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
]
