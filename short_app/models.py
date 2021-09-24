from django.db import models

class UrlData(models.Model):
    url = models.CharField('Длинная ссылка', max_length=255)
    slug = models.CharField('Короткая ссылка', max_length=20,unique=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
