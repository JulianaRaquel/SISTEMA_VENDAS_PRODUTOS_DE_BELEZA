from django.urls import path
from .views import home, marca, produto


urlpatterns = [
    path('home/', home, name='home'),
    path('marca/<int:id>', marca, name='marca'),
    path('produto/<int:id>', produto, name="produto"),
]