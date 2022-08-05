from django.urls import path
from usuarios.views import CriarPerfil, Update, Login, Logout

urlpatterns = [
    path('criar_perfil/', CriarPerfil.as_view(), name='criar_perfil'),
    path('update/', Update.as_view(), name='update'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]