# Generated by Django 3.0.2 on 2020-02-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200201_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.TextField(default='', null=True),
        ),
    ]
