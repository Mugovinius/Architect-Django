# Generated by Django 4.1.5 on 2023-02-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
