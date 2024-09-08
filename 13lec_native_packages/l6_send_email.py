# Simple Mail Transfer Protocol (SMTP)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
from pathlib import Path

path = Path("img/cat.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "correo_from@gmail.com"
mensaje["to"] = "correo_to@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login(user="correo_login@gmail.com", password="")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
