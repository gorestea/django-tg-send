from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class TelegramChannelForm(forms.ModelForm):
    class Meta:
        model = TelegramChannel
        fields = '__all__'

class NewCarForm(forms.ModelForm):
    class Meta:
        model = New_Car
        fields = '__all__'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Фотографии')

    class Meta:
        model = Images
        fields = ('image',)

# class AdvertisementsForm(forms.Form):
#     channels = forms.ModelMultipleChoiceField(
#         queryset=TelegramChannel.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         label='Выберите каналы для выгрузки объявлений'
#     )