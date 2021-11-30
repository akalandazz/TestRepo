# Generated by Django 3.2.9 on 2021-11-29 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_shift_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiddayShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('on_duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_midday_shifts', to='persons.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MorningShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('on_duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_moning_shifts', to='persons.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NightShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('on_duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_night_shifts', to='persons.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('midday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midday_shifts', to='persons.middayshift')),
                ('morning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morning_shifts', to='persons.morningshift')),
                ('nigth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='night_shifts', to='persons.nightshift')),
            ],
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]