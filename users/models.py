from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Пользователь' , on_delete=models.CASCADE)
    email_field = models.EmailField('Почта', default='priver@gmail.com')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'



    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

# class UrlData(models.Model):
#     url = models.CharField('Длинная ссылка', max_length=255, unique=True)
#     slug = models.CharField('Короткая ссылка', max_length=15)

#     def __str__(self):
#         return self.url

#     class Meta:
#         verbose_name = 'Ссылка'
#         verbose_name_plural = 'Ссылки'