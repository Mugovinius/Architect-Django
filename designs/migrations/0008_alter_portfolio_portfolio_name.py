# Generated by Django 4.1.5 on 2023-02-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0007_alter_portfolio_portfolio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_name',
            field=models.TextField(),
        ),
    ]
