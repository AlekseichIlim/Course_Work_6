# Generated by Django 4.2.2 on 2024-09-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0005_alter_dispatch_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dispatch",
            name="next_sent_date_time",
            field=models.DateTimeField(
                blank=True,
                default=None,
                null=True,
                verbose_name="дата и время следующей отправки",
            ),
        ),
    ]