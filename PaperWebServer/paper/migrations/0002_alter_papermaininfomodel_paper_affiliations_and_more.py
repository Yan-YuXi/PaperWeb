# Generated by Django 4.2.4 on 2023-08-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paper", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="papermaininfomodel",
            name="paper_affiliations",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="papermaininfomodel",
            name="paper_keywords",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
