import cv2
import face_recognition

def capturar_video():
    video_capture = cv2.VideoCapture(0)  # Captura da webcam

    while True:
        ret, frame = video_capture.read()  # Lê um quadro de vídeo
        rgb_frame = frame[:, :, ::-1]  # Converte de BGR para RGB

        # Detecta localizações de faces
        face_locations = face_recognition.face_locations(rgb_frame)
        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
            break

    video_capture.release()
    cv2.destroyAllWindows()

# Testar a captura de vídeo
if __name__ == "__main__":
    capturar_video()