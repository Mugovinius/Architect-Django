# Generated by Django 4.1.5 on 2023-02-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0003_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_name',
            field=models.CharField(max_length=100, verbose_name='Portfolio Name'),
        ),
    ]
