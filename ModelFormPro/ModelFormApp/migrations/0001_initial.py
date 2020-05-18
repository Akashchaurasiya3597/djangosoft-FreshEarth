# Generated by Django 3.0 on 2020-02-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(blank=True, max_length=100)),
                ('Sales', models.IntegerField(blank=True)),
                ('Mobile_number', models.BigIntegerField(blank=True)),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('Location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
