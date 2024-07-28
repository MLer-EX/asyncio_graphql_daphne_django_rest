from django.contrib import admin

from my_app.models import Item


@admin.register(Item)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'field2', 'field3')


