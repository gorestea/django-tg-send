# Generated by Django 4.2.3 on 2023-07-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('cabin', models.CharField(max_length=100)),
                ('formula', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('axle', models.CharField(max_length=100)),
                ('euro_class', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(upload_to='car_photos')),
            ],
        ),
    ]
