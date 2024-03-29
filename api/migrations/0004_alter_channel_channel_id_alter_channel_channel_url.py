# Generated by Django 5.0.2 on 2024-03-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_channel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="channel_id",
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="channel_url",
            field=models.URLField(unique=True),
        ),
    ]
