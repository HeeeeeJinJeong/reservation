# Generated by Django 2.2.6 on 2019-10-10 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20191010_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
