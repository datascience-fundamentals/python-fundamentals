from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
from pathlib import Path
from string import Template

plantilla = Path("doc/plantilla.html").read_text(encoding="utf-8")

template = Template(plantilla)
params = {"usuario": "Chanchito Feliz"}
data = template.substitute(usuario="Chachito Ilusionado")

path = Path("img/cat.jpg")
imagen = MIMEImage(path.read_bytes())
cuerpo = MIMEText(data, "html")
mensaje = MIMEMultipart()
mensaje["from"] = "correo_from@gmail.com"
mensaje["to"] = "correo_to@gmail.com"
mensaje["subject"] = "Hola mundo"
mensaje.attach(cuerpo)
mensaje.attach(imagen)

with SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login(user="correo_login@gmail.com", password="")
    smtp.send_message(mensaje)
    print("Se envio el correo con exito")
