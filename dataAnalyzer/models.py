from django.db import models


# Model for cattle table
class Weighing(models.Model):
    weight = models.FloatField(
        null=False,
        blank=False
    )
    date = models.DateField(
        null=False,
        blank=False
    )

class Cattle(models.Model):
    id = models.IntegerField(
        null=False,
        blank=False,
        primary_key=True
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
