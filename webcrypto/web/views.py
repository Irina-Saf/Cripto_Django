from django.shortcuts import render
from info.models import TgUser


def index(request):
    all_users = TgUser.objects.all()

    context = {
        'all_users': all_users,
    }
    return render(request, 'web/index.html', context)
