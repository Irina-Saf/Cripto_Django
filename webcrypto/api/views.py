from info.models import TgUser
from rest_framework import viewsets
from api.serializers import TgUserSerializer
from rest_framework.permissions import AllowAny


class TgUserViewSet(viewsets.ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = (AllowAny, )
