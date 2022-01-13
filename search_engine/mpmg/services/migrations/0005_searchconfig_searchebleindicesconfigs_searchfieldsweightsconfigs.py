# Generated by Django 3.0.5 on 2020-10-08 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200928_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results_per_page', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='SearchebleIndicesConfigs',
            fields=[
                ('index', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('searchble', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchFieldsWeightsConfigs',
            fields=[
                ('field', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=50)),
                ('weight', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('searchble', models.BooleanField(default=True)),
            ],
        ),
    ]
