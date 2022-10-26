from django.db import models
from django.utils.safestring import mark_safe

class Marca(models.Model):
    marca = models.CharField(max_length=30)

    def __str__(self):
        return self.marca

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    img = models.ImageField(upload_to='post_img')
    volume = models.CharField(max_length=8, default='blank')
    descricao = models.TextField()
    preco = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self):
        return self.nome