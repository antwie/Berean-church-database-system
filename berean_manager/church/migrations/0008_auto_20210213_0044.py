# Generated by Django 2.2.10 on 2021-02-13 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0007_auto_20201124_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='baptism_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='father_deceased',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='mother_deceased',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='Home_town',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='Spouse_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='baptism',
            field=models.CharField(blank=True, default='Yes', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='baptism_date',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='baptism_place',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(blank=True, default='Ghana', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_join',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='digital_address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_full_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='emergency_phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='fathers_location',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='fathers_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='house_number',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(blank=True, default='Single', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='mothers_location',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='mothers_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='number_of_children',
            field=models.CharField(blank=True, default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='other_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='place_of_birth',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='region',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
