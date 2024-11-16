# Generated by Django 5.1.3 on 2024-11-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='card',
            name='expiration_month',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='expiration_year',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
