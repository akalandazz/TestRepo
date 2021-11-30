# Generated by Django 3.2.4 on 2021-11-29 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_alter_shift_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='description',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shift_end',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shift_start',
        ),
        migrations.AddField(
            model_name='shift',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
