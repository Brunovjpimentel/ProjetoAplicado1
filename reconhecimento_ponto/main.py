from database import criar_banco_de_dados, cadastrar_colaborador
from reconhecimento_facial import capturar_video
from envio_email import enviar_email

def main():
    criar_banco_de_dados()
    # Exemplo de cadastro de colaborador
    cadastrar_colaborador('João Silva', 'joao@empresa.com', 'caminho_para_foto_joao.jpg')

    # Iniciar captura de vídeo e reconhecimento facial
    capturar_video()

    # Exemplo de envio de e-mail
    enviar_email('joao@empresa.com', 'Confirmação de Registro de Ponto', 'Seu ponto foi registrado com sucesso.')

if __name__ == "__main__":
    main()