# Generated by Django 2.2.5 on 2019-10-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0002_auto_20191003_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ememail',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
