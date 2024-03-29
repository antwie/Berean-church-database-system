# Generated by Django 2.2.10 on 2021-02-13 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0007_auto_20201124_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
