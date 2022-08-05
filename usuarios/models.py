from django.contrib.auth.models import User
from django.db import models

class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idade = models.IntegerField()
    data = models.DateTimeField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        pass

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
