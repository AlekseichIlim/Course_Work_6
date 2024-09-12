# Generated by Django 4.2.2 on 2024-09-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0015_client_owner_message_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dispatch",
            options={
                "ordering": ("title", "first_sent_date_time", "status"),
                "permissions": [
                    ("can_edit_status", "Can edit status"),
                    ("can_edit_is_activ", "Can edit is activ"),
                ],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.AddField(
            model_name="dispatch",
            name="is_activ",
            field=models.BooleanField(default=True, verbose_name="учится"),
        ),
    ]