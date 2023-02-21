# Generated by Django 4.1.5 on 2023-02-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=30, verbose_name='Service Name')),
                ('description', models.TextField()),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
