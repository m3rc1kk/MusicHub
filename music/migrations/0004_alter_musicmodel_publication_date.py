# Generated by Django 4.2.7 on 2023-12-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_musicmodel_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicmodel',
            name='publication_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
