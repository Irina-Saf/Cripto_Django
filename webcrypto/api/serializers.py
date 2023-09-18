from rest_framework import serializers

from info.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    """Список ингредиентов."""

    class Meta:
        model = TgUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'telegram_id',
            'phone_number',
            'is_premium'
        )
