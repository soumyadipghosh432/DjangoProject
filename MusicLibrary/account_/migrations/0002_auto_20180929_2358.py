# Generated by Django 2.1.1 on 2018-09-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
