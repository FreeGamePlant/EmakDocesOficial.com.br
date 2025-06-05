from flask import Flask, request
import smtplib
from email.message import EmailMessage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ative o CORS depois de criar o app

EMAIL_USER = 'andreia2017depa@gmail.com'
EMAIL_PASS = 'rzgmlrgesxaojsyh'
EMAIL_TO = 'emakdoces@gmail.com'

@app.route('/enviar-curtida', methods=['POST'])
def enviar_curtida():
    produto = request.form.get('produto', 'Produto desconhecido')
    msg = EmailMessage()
    msg.set_content(f'Um produto foi curtido: {produto}')
    msg['Subject'] = 'Produto curtido no site!'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        return 'ok'
    except Exception as e:
        print('Erro ao enviar e-mail:', e)
        return 'erro', 500

if __name__ == '__main__':
    app.run(debug=True)