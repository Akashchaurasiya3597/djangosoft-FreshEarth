# Generated by Django 3.0 on 2020-02-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelFormApp', '0006_customer_model_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_model',
            name='picture',
            field=models.ImageField(blank=True, upload_to='content/'),
        ),
    ]
