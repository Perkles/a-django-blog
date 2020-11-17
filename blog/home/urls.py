from django.urls import path
from .views import home_page_rendering

urlpatterns = [
    path('', home_page_rendering, name="home"),
]