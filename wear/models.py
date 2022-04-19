from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

    def __str__(self) -> str:
        return self.name


class Wear(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='wear/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Добавлен')
    uploaded = models.DateTimeField(auto_now=True, verbose_name = 'Изменен')

    def get_absolute_url(self):
        return reverse('wear:product', args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = self.name
        return super(Wear, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Wear'
        verbose_name_plural = 'Wears'

    def __str__(self) -> str:
            return self.name