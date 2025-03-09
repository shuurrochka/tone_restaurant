from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='dishes/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"