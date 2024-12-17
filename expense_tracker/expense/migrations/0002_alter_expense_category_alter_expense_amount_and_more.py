# Generated by Django 5.1.4 on 2024-12-17 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("expense", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("Food", "Food"),
                    ("Travel", "Travel"),
                    ("Utilities", "Utilities"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="amount",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="expense",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.user"
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
