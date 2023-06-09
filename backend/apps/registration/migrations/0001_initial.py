# Generated by Django 4.1.7 on 2023-04-21 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(default="", max_length=255)),
                ("phone", models.CharField(default="", max_length=10)),
                ("subject", models.TextField(default="")),
                ("message", models.TextField(default="")),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(default="", max_length=255)),
                ("email", models.EmailField(default="", max_length=254)),
                ("password", models.CharField(default="", max_length=128)),
                ("first_name", models.CharField(default="", max_length=255)),
                ("last_name", models.CharField(default="", max_length=255)),
                ("address", models.CharField(default="", max_length=255)),
                ("phone_number", models.CharField(default="", max_length=10)),
                (
                    "father_name",
                    models.CharField(default="", max_length=255, null=True),
                ),
                (
                    "mother_name",
                    models.CharField(default="", max_length=255, null=True),
                ),
                ("short_bio", models.TextField(default="")),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        default="",
                        max_length=6,
                    ),
                ),
                (
                    "blood_group",
                    models.CharField(
                        choices=[
                            ("A-", "A-"),
                            ("A+", "A+"),
                            ("B-", "B-"),
                            ("B+", "B+"),
                            ("AB-", "AB-"),
                            ("AB+", "AB+"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                        ],
                        default="",
                        max_length=3,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Student", "Student"),
                            ("Teacher", "Teacher"),
                            ("Parent", "Parent"),
                            ("Admain", "Admain"),
                        ],
                        default="",
                        max_length=15,
                    ),
                ),
                (
                    "religion",
                    models.CharField(
                        choices=[
                            ("Muslim", "Muslim"),
                            ("Christian", "Christian"),
                            ("Jewish", "Jewish"),
                        ],
                        default="",
                        max_length=10,
                    ),
                ),
                ("if_logged", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
