# Generated by Django 4.1.4 on 2023-09-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataAnalyzer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='birthDay',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='weighing',
            name='date',
            field=models.CharField(max_length=40),
        ),
    ]