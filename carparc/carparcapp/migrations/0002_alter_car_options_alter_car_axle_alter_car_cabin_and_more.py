# Generated by Django 4.2.3 on 2023-07-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-price'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='car',
            name='axle',
            field=models.CharField(max_length=100, verbose_name='Мосты'),
        ),
        migrations.AlterField(
            model_name='car',
            name='cabin',
            field=models.CharField(max_length=100, verbose_name='Кабина'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=100, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='euro_class',
            field=models.CharField(max_length=100, verbose_name='Евро-класс'),
        ),
        migrations.AlterField(
            model_name='car',
            name='formula',
            field=models.CharField(max_length=100, verbose_name='Формула'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=100, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='car_photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.CharField(max_length=100, verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=100, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Тип'),
        ),
    ]
