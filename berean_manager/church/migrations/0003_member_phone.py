# Generated by Django 2.2.10 on 2020-07-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_auto_20200728_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
