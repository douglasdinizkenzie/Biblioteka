# Generated by Django 4.2.1 on 2023-05-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_user_copies_user_loans"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="blocked_until",
            field=models.DateTimeField(default=None),
        ),
    ]
