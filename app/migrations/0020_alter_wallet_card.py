# Generated by Django 5.0 on 2023-12-11 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0019_card_wallet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="card",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.card",
            ),
        ),
    ]
