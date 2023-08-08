import asyncio
import json
import sys

from django.forms import modelformset_factory

sys.path.append('C:/Users/123b/Desktop/djangoparcer/carparc')
from tgbot import send_to_telegram
import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from threading import Thread, Event
from .models import *
from .forms import *

def home(request):
    cars = Car.objects.all()
    new_cars = New_Car.objects.all()
    return render(request, 'home.html', {'cars': cars, 'new_cars': new_cars})

def choose_car(request):
    return render(request, 'add.html')
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def new_add_car(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = NewCarForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(car=post_form, image=image)
                    photo.save()
            # use django messages framework
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = NewCarForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'new_add_car.html',
                  {'postForm': postForm, 'formset': formset})

def car_details(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        # Найдите запись по идентификатору и удалите ее из базы данных
        car.delete()
        return redirect('home')
    return render(request, 'car_details.html', {'car': car})

def new_car_details(request, pk):
    new_car = get_object_or_404(New_Car, pk=pk)
    new_car_photos = Images.objects.filter(car=pk)
    if request.method == 'POST':
        # Найдите запись по идентификатору и удалите ее из базы данных
        new_car.delete()
        return redirect('home')
    return render(request, 'new_car_details.html', {'new_car': new_car, 'images': new_car_photos})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CarForm(instance=car)
    return render(request, 'add_car.html', {'form': form})

def new_car_edit(request, pk):
    new_car = get_object_or_404(New_Car, pk=pk)
    if request.method == 'POST':
        form = NewCarForm(request.POST, request.FILES, instance=new_car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewCarForm(instance=new_car)
    return render(request, 'new_add_car.html', {'form': form})

# def upload_excel(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('excel_file')
#         if not excel_file:
#             return HttpResponse('Ничего не было загружено')
#         if not excel_file.name.endswith('.xlsx'):
#             return HttpResponse('Выберите файл Excel (.xlsx)')
#         df = pd.read_excel(excel_file)
#         for index, row in df.iterrows():
#             Car.objects.create(
#                 make=row['Модель'],
#                 type=row['Тип'],
#                 cabin=row['Кабина'],
#                 formula=row['Формула'],
#                 engine=row['Двигатель'],
#                 power=row['Мощность'],
#                 transmission=row['КПП'],
#                 axle=row['Мосты'],
#                 euro_class=row['Евро класс']
#             )
#         return HttpResponse('/')
#     else:
#         return render(request, 'upload_excel.html')

def channel_list(request):
    channels = TelegramChannel.objects.all()
    channels_list = []
    for channel in channels:
        channels_list.append(str(channel))
    with open('channels.json', 'w', encoding='utf-8') as file:
        json.dump(channels_list, file, indent=4, ensure_ascii=False)
    return render(request, 'channel_list.html', {'channels': channels})

def channel_detail(request, pk):
    channel = get_object_or_404(TelegramChannel, pk=pk)
    if request.method == 'POST':
        channel.delete()
        return HttpResponseRedirect('/channels/')
    return render(request, 'channel_detail.html', {'channel': channel})

def channel_create(request):
    if request.method == 'POST':
        form = TelegramChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/channels/')
    else:
        form = TelegramChannelForm()
    return render(request, 'channel_form.html', {'form': form})

stop_event = Event()
async def start_auto(request):
    global stop_event
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()
    await send_to_telegram(loop, stop_event)
    return HttpResponseRedirect('/')

async def stop_auto(request):
    global stop_event
    stop_event.set()
    print('Программа остановлена!')
    return HttpResponseRedirect('/')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def undercategory_list(request, cat_slug):
    category = Category.objects.get(slug=cat_slug)
    undercategories = UnderCategory.objects.filter(category=category)
    return render(request, 'undercategory_list.html', {'undercategories': undercategories})

# def select_channels(request):
#     if request.method == 'POST':
#         form = AdvertisementsForm(request.POST)
#         if form.is_valid():
#             result = form.cleaned_data
#             new = TelegramChannel(
#                 name=result
#             )
#             new.save()
#             return redirect('home')
#     else:
#         form = AdvertisementsForm()
#     return render(request, 'add_car.html', {'form': form})





