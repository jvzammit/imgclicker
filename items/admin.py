
from django.contrib import admin
from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'title', 'image_url']


admin.site.register(Item, ItemAdmin)
