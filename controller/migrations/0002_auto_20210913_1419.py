# Generated by Django 3.2.7 on 2021-09-13 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controller',
            options={'ordering': ('created',)},
        ),
        migrations.CreateModel(
            name='ElectricalParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rms_voltage', models.DecimalField(decimal_places=5, max_digits=10)),
                ('rms_current', models.DecimalField(decimal_places=5, max_digits=10)),
                ('active_power', models.DecimalField(decimal_places=5, max_digits=10)),
                ('reactive_power', models.DecimalField(decimal_places=5, max_digits=10)),
                ('phase_connection', models.CharField(blank=True, max_length=1)),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('controller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='controller.controller')),
            ],
            options={
                'ordering': ('controller',),
            },
        ),
    ]
