# Generated by Django 5.0.2 on 2024-02-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="job_uuid",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
