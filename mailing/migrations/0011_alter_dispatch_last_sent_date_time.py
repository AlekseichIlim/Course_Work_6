# Generated by Django 4.2.2 on 2024-09-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0010_alter_dispatch_first_sent_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dispatch",
            name="last_sent_date_time",
            field=models.DateTimeField(
                default=None, verbose_name="дата и время последней отправки"
            ),
        ),
    ]