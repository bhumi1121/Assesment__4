# Generated by Django 4.2.4 on 2023-08-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=100)),
                ("Content", models.CharField(max_length=100)),
                ("Created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
        ),
    ]