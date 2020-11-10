from django.db import models


class Articles(models.Model):
    title = models.TextField('Название')
    descriptions = models.TextField('Описание')
    image = models.ImageField()
    date = models.DateTimeField('Время проведения')
    location = models.TextField('Место проведения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Собития'
        verbose_name_plural ='Собития'
