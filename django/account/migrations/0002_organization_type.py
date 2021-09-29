# Generated by Django 3.2.7 on 2021-09-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="type",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "機械科"), (2, "電機科"), (4, "情報科"), (8, "環境科"), (16, "建築科"), (32, "部活動")],
                null=True,
                verbose_name="type",
            ),
        ),
    ]
