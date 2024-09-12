import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Dispatch, Attempts


def send_mailing(mailing, current_datetime):

    try:
        send_mail(subject=mailing.message.title_message,
                  message=mailing.message.body_message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[client.email for client in mailing.clients.all()],
                  fail_silently=False)

        first_time = current_datetime
        if mailing.periodicity == 'раз в день':
            mailing.next_sent_date_time = first_time + timedelta(days=1)
        elif mailing.periodicity == 'раз в неделю':
            mailing.next_sent_date_time = first_time + timedelta(weeks=1)
        else:
            mailing.next_sent_date_time = first_time + timedelta(days=30)
        Attempts.objects.create(datetime=current_datetime,
                                status=True,
                                dispatch=mailing,
                                mail_response='Рассылка прошла успешно')
    except smtplib.SMTPException as e:
        Attempts.objects.create(datetime=current_datetime,
                                status=False,
                                dispatch=mailing,
                                mail_response=str(e))


def start_send_mailing():
    """Функция отправки рассылки"""

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Dispatch.objects.filter(last_sent_date_time__gt=current_datetime)

    for mailing in mailings:
        if mailing.is_activ:
            if mailing.last_sent_date_time:
                if mailing.last_sent_date_time > current_datetime:
                    mailing.mailing_status = 'завершена'
                    mailing.save()
            if mailing.status == 'запущена':
                if mailing.first_sent_date_time == current_datetime or mailing.last_sent_date_time == current_datetime:
                    send_mailing(mailing, current_datetime)
            elif mailing.status == 'создана':
                mailing.status = 'запущена'
                send_mailing(mailing, current_datetime)
            mailing.save()
        else:
            continue
