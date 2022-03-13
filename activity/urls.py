from django.urls import path

from .views import LoginView, EventsView, PublicationsView


urlpatterns = [
    path('auth/', LoginView.as_view(), name='auth'),
    path('events/', EventsView.as_view(), name='events'),
    path('publications/', PublicationsView.as_view(), name='publications'),
]