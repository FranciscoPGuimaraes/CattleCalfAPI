# Generated by Django 4.2.4 on 2023-09-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
