# Generated by Django 4.2.1 on 2023-05-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_user_blocked_until"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="blocked_until",
            field=models.CharField(default=None, max_length=30),
        ),
    ]
