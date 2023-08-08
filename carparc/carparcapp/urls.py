from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('choose_car/', choose_car, name='choose_car'),
    path('add_car/', add_car, name='add_car'),
    path('new_add_car/', new_add_car, name='new_add_car'),
    path('car/<int:pk>/', car_details, name='car_details'),
    path('new_car/<int:pk>/', new_car_details, name='new_car_details'),
    path('car/<int:pk>/edit', car_edit, name='car_edit'),
    path('new_car/<int:pk>/edit', new_car_edit, name='new_car_edit'),
    # path('upload_excel/', upload_excel, name='upload_excel'),
    path('channels/', channel_list, name='channel_list'),
    path('channel_create/', channel_create, name='channel_create'),
    path('channel/<int:pk>/', channel_detail, name='channel_detail'),
    path('channel/<int:pk>/', channel_detail, name='channel_detail'),
    path('start/', start_auto, name='start'),
    path('stop/', stop_auto, name='stop'),
    path('categories/', category_list, name='category_list'),
    # path('add_tg/', select_channels, name='select_channels'),
    path('categories/<slug:cat_slug>/', undercategory_list, name='undercategory_list')
]