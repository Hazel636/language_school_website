# Generated by Django 3.2.25 on 2024-06-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
