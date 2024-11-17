import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, corpo):
    remetente = 'marquezam.marques@xmti.com.br'
    senha = '**********'
    servidor_smtp = 'email-ssl.com.br'
    porta_smtp = 465

    # Criação da mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        # Conectando ao servidor SMTP usando SSL
        with smtplib.SMTP_SSL(servidor_smtp, porta_smtp) as servidor:
            servidor.login(remetente, senha)  # Autenticando com o servidor
            servidor.send_message(mensagem)
            print("E-mail enviado com sucesso!")
    except smtplib.SMTPAuthenticationError:
        print("Falha ao autenticar: Verifique suas credenciais e tente novamente.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Teste de envio de e-mail
if __name__ == "__main__":
    enviar_email('marquezam.81@gmail.com', 'Teste de E-mail', 'Este é um teste de envio de e-mail usando SSL/TLS.')