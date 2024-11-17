import cv2

def testar_camera():
    # Acessa a câmera (0 é geralmente a câmera padrão)
    #camera = cv2.VideoCapture(0)
    #camera = cv2.VideoCapture(1)  # Tente com 1 ou outros índices
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print("Não foi possível acessar a câmera.")
        return
    
    print("Câmera acessada com sucesso. Pressione 'q' para sair.")
    
    while True:
        # Captura o frame
        ret, frame = camera.read()
        
        if not ret:
            print("Não foi possível capturar a imagem.")
            break
        
        # Exibe o frame
        cv2.imshow("Frame", frame)
        
        # Sai do loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera a câmera e fecha as janelas
    camera.release()
    cv2.destroyAllWindows()

# Chama a função de teste
testar_camera()