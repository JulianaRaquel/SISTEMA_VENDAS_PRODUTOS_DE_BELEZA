import os.path
from PIL import Image
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    img = models.ImageField(upload_to='post_img')
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco = models.FloatField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)


    # método para redimensionar as imagens
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            print('Retornando, largura original menor que nova largura')
            img_pil.close()
            return

        new_heigth = round((new_width * original_height)/original_width)

        new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug


        super().save(*args, **kwargs)

        max_image_size = 800

        if self.img:
            self.resize_image(self.img, max_image_size)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.img.url}">'

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'