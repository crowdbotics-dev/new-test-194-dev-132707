from django.conf import settings
from django.db import models


class T1(models.Model):
    "Generated Model"
    t1 = models.BigIntegerField()


class T2(models.Model):
    "Generated Model"
    t2 = models.BigIntegerField()
    t3 = models.BigIntegerField(
        null=True,
        blank=True,
    )
    t4 = models.BigIntegerField(
        null=True,
        blank=True,
    )
