from django.urls import path

from cms.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),  # Первая страница
]