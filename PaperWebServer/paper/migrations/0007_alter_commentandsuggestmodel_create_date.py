# Generated by Django 4.2.4 on 2023-09-11 09:24

from django.db import migrations, models
import utils


class Migration(migrations.Migration):
    dependencies = [
        ("paper", "0006_commentandsuggestmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentandsuggestmodel",
            name="create_date",
            field=models.DateTimeField(default=utils.utcnow),
        ),
    ]
