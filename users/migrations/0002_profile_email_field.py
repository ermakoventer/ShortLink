# Generated by Django 3.2.5 on 2021-08-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_field',
            field=models.EmailField(default='11111', max_length=254, verbose_name='Почта'),
        ),
    ]
