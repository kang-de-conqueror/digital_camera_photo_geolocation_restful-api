# Generated by Django 2.2.11 on 2020-04-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_geotag', '0003_auto_20200408_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_data',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.TextField(null=True),
        ),
    ]
