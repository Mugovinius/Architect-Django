# Generated by Django 4.1.5 on 2023-02-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0009_alter_portfolio_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_name',
            field=models.CharField(max_length=50, verbose_name='Portfolio Name'),
        ),
    ]
