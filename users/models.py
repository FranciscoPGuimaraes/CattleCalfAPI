from django.db import models


class User(models.Model):
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        auto_created=False,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=45,
        null=False,
        blank=False
    )
    password = models.CharField(
        max_length=45,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=45,
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )