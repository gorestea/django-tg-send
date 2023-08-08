from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Car)
admin.site.register(TelegramChannel)
admin.site.register(New_Car)
admin.site.register(Images)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UnderCategory, CategoryAdmin)
