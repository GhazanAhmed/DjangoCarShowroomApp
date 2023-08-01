# Generated by Django 4.2.3 on 2023-07-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_showroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="showroom",
            options={"verbose_name_plural": "Showroom"},
        ),
        migrations.AddField(
            model_name="engine",
            name="name",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name="engine",
            name="specs",
            field=models.CharField(max_length=150, null=True),
        ),
    ]