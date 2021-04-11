from django.urls import path

from .views import CountdownCreateView, CountdownDetailView, DashBoardView, CountdownDeleteView, CountdownUpdateView

app_name = 'countdown_core'

urlpatterns = [
    path('create/', CountdownCreateView.as_view(), name='create'),
    path('<int:pk>/', CountdownDetailView.as_view(), name='detail'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('<int:pk>/delete', CountdownDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit', CountdownUpdateView.as_view(), name='edit'),
]
