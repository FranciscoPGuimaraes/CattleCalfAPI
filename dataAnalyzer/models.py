from django.db import models


# Model for cattle table
class Weighing(models.Model):
    idWeighing = models.IntegerField(
        primary_key=True,
        auto_created=True,
        null=False,
        blank=False
    )
    weight = models.FloatField(
        null=False,
        blank=False
    )
    date = models.DateField(
        null=False,
        blank=False
    )


class Cattle(models.Model):
    idCattle = models.IntegerField(
        null=False,
        blank=False,
        primary_key=True,
        auto_created = True,
    )

    breed = models.CharField(
        max_length=45,
        null=False,
        blank=False
    )
    birthDay = models.DateField(
        null=False,
        blank=False
    )
    weight = models.ForeignKey(
        Weighing,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class Type(models.Model):
    idType = models.IntegerField(
        auto_created=True,
        primary_key=True,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )


class Expense(models.Model):
    idExpense = models.IntegerField(
        auto_created=True,
        primary_key=True,
        null=False,
        blank=False
    )
    amount = models.FloatField(
        null=False,
        blank=False
    )
    date = models.DateField(
        null=False,
        blank=False
    )
    type_idType = models.ForeignKey(
        Type,
        on_delete=models.DO_NOTHING,
        null=False
    )
