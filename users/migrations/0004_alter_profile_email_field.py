# Generated by Django 3.2.5 on 2021-08-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_email_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_field',
            field=models.EmailField(default='priver@gmail.com', max_length=254, verbose_name='Почта'),
        ),
    ]