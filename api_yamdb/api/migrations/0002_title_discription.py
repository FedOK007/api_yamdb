# Generated by Django 3.2 on 2023-01-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='discription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
