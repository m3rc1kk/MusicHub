# Generated by Django 4.2.7 on 2023-12-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_musicmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicmodel',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
