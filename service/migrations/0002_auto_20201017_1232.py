# Generated by Django 3.1.2 on 2020-10-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
