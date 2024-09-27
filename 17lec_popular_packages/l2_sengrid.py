import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

email = os.environ.get("SENGRID_EMAIL")
print(email)

mensaje = Mail(
    from_email=email,
    to_emails="to@correo.com",
    subject="Correo de prueba",
    html_content="Curso de <b>Ultimate Python</b>"
)

try:
    api_key = os.environ.get("SENGRID_API_KEY")
    print(api_key)
    sg = SendGridAPIClient(api_key)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers,
        respuesta,
    )
except Exception as e:
    print(e)
else:
    print("se envio correo con exito")
