# Generated by Django 3.2.11 on 2022-07-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=10000000),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]