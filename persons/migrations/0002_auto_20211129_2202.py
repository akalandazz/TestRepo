# Generated by Django 3.2.4 on 2021-11-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='date',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shift_name',
        ),
        migrations.AddField(
            model_name='shift',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shift',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
