# Generated by Django 3.2.25 on 2024-06-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='accommodation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='age_limit',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='recreation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='accommodation_options',
            field=models.ManyToManyField(null=True, to='listings.AccommodationOption'),
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.category'),
        ),
        migrations.AddField(
            model_name='listing',
            name='headline',
            field=models.ManyToManyField(blank=True, related_name='listings', to='listings.Headline'),
        ),
    ]
