# Generated by Django 2.2.10 on 2021-04-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0012_imagecontainer_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]