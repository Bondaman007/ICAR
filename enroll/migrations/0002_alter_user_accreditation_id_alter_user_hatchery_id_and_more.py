# Generated by Django 4.1.5 on 2023-02-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accreditation_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='hatchery_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='year_of_accreditation',
            field=models.IntegerField(),
        ),
    ]
