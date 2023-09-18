from django import forms

from info.models import TgUser


class TgUserForm(forms.ModelForm):
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
