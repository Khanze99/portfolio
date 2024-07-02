
import asyncio
from celery import shared_task
from django.conf import settings
from telegram import Bot

from .models import ServiceRequest


bot = Bot(settings.TG_SECURE_TOKEN)


@shared_task
def send_event_tg(service_request_id):
    """Отправка заявки в тг канал оповещений"""
    async def send(text):
        await bot.send_message(settings.TG_CHAT_ID, text=text)
    service_request: ServiceRequest = ServiceRequest.objects.get(id=service_request_id)
    text = f"""
    ✅✅✅ Заявка номер: {service_request.id}\n
    Заявитель 👤: {service_request.customer_request_name} - {service_request.email_customer}\n
    Номер телефона 🔢: {service_request.customer_phone_number}\n
    Наименование 🆕: {service_request.title}\n
    Описание 🟢: {service_request.description}\n
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send(text))

    service_request.is_viewed = True
    service_request.save()
