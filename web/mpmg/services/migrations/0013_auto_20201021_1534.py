# Generated by Django 3.0.5 on 2020-10-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20201021_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchableindicesconfigs',
            name='group',
            field=models.CharField(choices=[('regular', 'regular'), ('replica', 'replica')], max_length=10),
        ),
        migrations.AlterField(
            model_name='searchableindicesconfigs',
            name='index_model',
            field=models.CharField(choices=[('Diario', 'Diario'), ('Processo', 'Processo')], max_length=50),
        ),
    ]
