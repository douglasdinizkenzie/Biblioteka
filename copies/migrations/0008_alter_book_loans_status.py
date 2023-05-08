# Generated by Django 4.2.1 on 2023-05-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0007_alter_copies_is_available"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book_loans",
            name="status",
            field=models.CharField(
                choices=[
                    ("Borrowed", "Borrowed"),
                    ("Returned", "Returned"),
                    ("Delayed", "Delayed"),
                ],
                default="Borrowed",
                max_length=10,
                null=True,
            ),
        ),
    ]