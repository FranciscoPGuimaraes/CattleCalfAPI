# Generated by Django 4.2.4 on 2023-09-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
    ]
