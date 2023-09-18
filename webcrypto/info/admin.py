from django.contrib import admin
from info.models import TgUser


@admin.register(TgUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'telegram_id',
        'phone_number',
        'is_premium'
    )

    search_fields = ('telegram_id',)
    empty_value_display = "-пусто-"
