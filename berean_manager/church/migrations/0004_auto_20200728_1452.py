# Generated by Django 2.2.10 on 2020-07-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.EmailField(max_length=100),
        ),
    ]
