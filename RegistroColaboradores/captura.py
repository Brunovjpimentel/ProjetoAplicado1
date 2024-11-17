import cv2
import os
from datetime import datetime

def capturar_imagem(colaborador_id):
    cam = cv2.VideoCapture(0)  # Inicializa a câmera USB
    ret, frame = cam.read()  # Captura uma imagem
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"imagens/{colaborador_id}_{timestamp}.jpg"
        cv2.imwrite(nome_arquivo, frame)
        cam.release()
        cv2.destroyAllWindows()
        return nome_arquivo
    else:
        cam.release()
        cv2.destroyAllWindows()
        raise Exception("Erro ao capturar imagem")
