from django.urls import path
from pages.views import homePageView   # Importamos la vista

urlpatterns = [
    path("", homePageView, name="home"),  # Ruta principal (http://127.0.0.1:8000/)
]
