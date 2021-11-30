# Generated by Django 3.2.9 on 2021-11-29 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_auto_20211130_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='middayshift',
            name='on_duty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_midday_shifts', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='morningshift',
            name='on_duty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_moning_shifts', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='nightshift',
            name='on_duty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_night_shifts', to='persons.person'),
        ),
    ]
