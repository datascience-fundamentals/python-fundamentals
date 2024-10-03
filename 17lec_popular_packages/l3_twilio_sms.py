import os
from twilio.rest import Client


sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
phone_from = os.environ.get("TWILIO_PHONE")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola mundo!",
    from_=phone_from,
    to="+99999999999",
)

print(mensaje)
