# Generated by Django 2.2 on 2020-06-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200628_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
