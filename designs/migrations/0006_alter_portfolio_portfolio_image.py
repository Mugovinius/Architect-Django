# Generated by Django 4.1.5 on 2023-02-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0005_alter_portfolio_portfolio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
