# Generated by Django 5.0.2 on 2024-06-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров'),
        ),
    ]