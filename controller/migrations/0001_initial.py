# Generated by Django 3.2.7 on 2021-09-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
