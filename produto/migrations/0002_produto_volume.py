# Generated by Django 4.1 on 2022-09-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='volume',
            field=models.CharField(default='blank', max_length=8),
        ),
    ]
