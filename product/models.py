from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):
    CATEGO = (
        ('Vestuário', 'Vestuário'),
        ('Calçados', 'Calçados'),
        ('Acessórios', 'Acessórios'),
        ('Eletrônicos', 'Eletrônicos'),
        ('Livros', 'Livros'),
        ('Usados', 'Usados'),
        ('Desconhecido', 'Desconhecido')
    )
    title = models.CharField(max_length=120)
    category = models.CharField(choices=CATEGO, max_length=25, default='Desconhecido')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True, default='')
    published = models.BooleanField(default=False)
    on_top = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'+f'{self.pk}'
            self.slug = slug
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        #return f'/produtos/{self.slug}/'
        return reverse("detail", kwargs={"slug":self.slug})




