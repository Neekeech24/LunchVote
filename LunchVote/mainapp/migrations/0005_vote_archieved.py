# Generated by Django 4.2.3 on 2023-07-31 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_alter_vote_slot"),
    ]

    operations = [
        migrations.AddField(
            model_name="vote",
            name="archieved",
            field=models.BooleanField(
                default=False
            ),
            preserve_default=False,
        ),
    ]
