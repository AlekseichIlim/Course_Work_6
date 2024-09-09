import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Dispatch, Attempts


def send_mailing():
    """Функция отправки рассылки"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Dispatch.objects.filter(next_send_date_time__lte=current_datetime).filter(
        status__in='LAUNCHED')

    for mailing in mailings:
        for client in mailing.clients.all():
            try:
                send_mail(subject=mailing.message.title_message,
                          message=mailing.message.body_message,
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[client.email],
                          fail_silently=False)

                mailing.first_sent_date_time = current_datetime
                if mailing.periodicity == 'DAILY':
                    mailing.next_send_date_time += timedelta(days=1)
                elif mailing.periodicity == 'WEEKLY':
                    mailing.next_send_date_time += timedelta(weeks=1)
                elif mailing.periodicity == 'MONTHLY':
                    mailing.next_send_date_time += timedelta(days=30)
                mailing.status = 'LAUNCHED'
                if mailing.last_send_date_time:
                    if mailing.next_send_date_time >= mailing.last_send_date_time:
                        mailing.status = 'COMPLETED'
                Attempts.objects.create(datetime=current_datetime,
                                        status=True,
                                        dispatch=mailing,
                                        mail_response='Письмо получено')
            except smtplib.SMTPException as e:
                Attempts.objects.create(datetime=current_datetime,
                                        status=False,
                                        dispatch=mailing,
                                        mail_response=str(e))
    mailing.status = 'COMPLETED'
    mailing.save()
