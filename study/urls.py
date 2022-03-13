from django.urls import path

from .views import ProfileView, TutorsView, PersonalCubView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),  # Профиль
    path('tutors/<str:subject>/', TutorsView.as_view(), name='tutors'), # Репетиторы
    path('personal_cub/', PersonalCubView.as_view(), name='personal_cub') # Репетиторы
]