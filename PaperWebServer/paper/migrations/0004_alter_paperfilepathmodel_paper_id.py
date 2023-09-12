# Generated by Django 4.2.4 on 2023-08-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("paper", "0003_alter_sourcedetailinfomodel_source_publisher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paperfilepathmodel",
            name="paper_id",
            field=models.ForeignKey(
                db_column="paper_id",
                on_delete=django.db.models.deletion.PROTECT,
                to="paper.papermaininfomodel",
            ),
        ),
    ]
