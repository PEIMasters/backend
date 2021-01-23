# Generated by Django 3.1.2 on 2021-01-23 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "address",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "zip_code",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "short_bio",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "profile_pic",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                ("id_number", models.IntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("request_date", models.DateTimeField(auto_now_add=True)),
                ("school", models.CharField(max_length=100)),
                ("course", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("requested_value_atto_dai", models.CharField(max_length=40)),
                ("description", models.CharField(max_length=5000)),
                ("state", models.IntegerField(default=0)),
                ("recipient_address", models.CharField(max_length=42)),
                (
                    "identifier",
                    models.CharField(blank=True, max_length=42, null=True),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IDVerifications",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "verification_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "person_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("validated", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_verification",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("is_public", models.BooleanField(default=False)),
                ("approved", models.BooleanField(default=False)),
                ("rejected", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=1000)),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.loan",
                    ),
                ),
            ],
        ),
    ]
