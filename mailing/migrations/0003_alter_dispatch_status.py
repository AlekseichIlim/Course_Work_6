# Generated by Django 4.2.2 on 2024-09-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_alter_dispatch_periodicity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dispatch",
            name="status",
            field=models.CharField(
                choices=[
                    ("создана", "создана"),
                    ("запущена", "отправлена"),
                    ("отменена", "отменена"),
                    ("завершена", "завершена"),
                    ("удалена", "удалена"),
                ],
                max_length=20,
                verbose_name="статус",
            ),
        ),
    ]
