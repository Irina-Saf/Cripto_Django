from django.db import models


class TgUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=30)
    telegram_id = models.IntegerField(unique=True, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    is_premium = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tg_User'


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'
