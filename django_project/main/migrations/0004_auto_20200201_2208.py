# Generated by Django 3.0.2 on 2020-02-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200201_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.TextField(default='', null=True, unique=True),
        ),
    ]