# Generated by Django 4.1.5 on 2023-02-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_alter_services_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_name', models.CharField(max_length=30, verbose_name='Portfolio Name')),
                ('portfolio_image', models.ImageField(upload_to='')),
                ('date', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=20)),
            ],
        ),
    ]
