from django.db import models

class TableBooking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    date = models.DateField(verbose_name="Дата бронирования")
    time = models.TimeField(verbose_name="Время бронирования")
    guests = models.PositiveIntegerField(verbose_name="Количество гостей")

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"