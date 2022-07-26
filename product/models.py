from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True, default='')
    published = models.BooleanField(default=False)
    on_top = models.BooleanField(default=False)
    slug = models.SlugField

    def __str__(self):
        return self.title