# Generated by Django 4.2.4 on 2023-08-29 07:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("paper", "0004_alter_paperfilepathmodel_paper_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="papermaininfomodel",
            old_name="paper_public_year",
            new_name="paper_publish_year",
        ),
    ]
