from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name='Модель')
    type = models.CharField(max_length=100, verbose_name='Тип')
    cabin = models.CharField(max_length=100, verbose_name='Кабина')
    formula = models.CharField(max_length=100, verbose_name='Формула')
    engine = models.CharField(max_length=100, verbose_name='Двигатель')
    power = models.CharField(max_length=100, verbose_name='Мощность')
    transmission = models.CharField(max_length=100, verbose_name='КПП')
    axle = models.CharField(max_length=100, verbose_name='Мосты')
    euro_class = models.CharField(max_length=100, verbose_name='Евро-класс')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    photo = models.ImageField(upload_to='car_photos', verbose_name='Фото', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', default=0)

    objects = models.Model

    def __str__(self):
        return self.make

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-price']

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    undercat = models.ForeignKey('UnderCategory', on_delete=models.PROTECT, verbose_name='Подкатегории', default=0)
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

class UnderCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'undercat_slug': self.slug})

class TelegramChannel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Канал')

    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
        ordering = ['name']

class New_Car(models.Model):
    description = models.CharField(max_length=2500, verbose_name='Текст продажи')

    objects = models.Model

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Новый автомобиль'
        verbose_name_plural = 'Новые автомобили'
        ordering = ['description']


def get_image_filename(instance, filename):
    title = instance.car.description
    slug = slugify(title)
    return "new_car_photos/%s-%s" % (slug, filename)


class Images(models.Model):
    car = models.ForeignKey(New_Car, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Фотографии')
    objects = models.Model
