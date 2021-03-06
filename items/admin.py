from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'is_public', 'category', 'created_at')
    list_filter = ('category',)
