from django.urls import path

from .views import CountdownCreateView, CountdownDetailView, DashBoardView, CountdownDeleteView, CountdownUpdateView, CountdownFinishedServiceView, ReactionServiceView, BookmarksServiceView

app_name = 'countdown_core'

urlpatterns = [
    path('create/', CountdownCreateView.as_view(), name='create'),
    path('<int:pk>/', CountdownDetailView.as_view(), name='detail'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('<int:pk>/delete', CountdownDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit', CountdownUpdateView.as_view(), name='edit'),
    path('<int:pk>/finished', CountdownFinishedServiceView.as_view(), name='finished'),
    path('<int:pk>/reaction/<int:reaction_id>', ReactionServiceView.as_view(), name='reaction'),
    path('<int:pk>/bookmark', BookmarksServiceView.as_view(), name='bookmark'),
]
