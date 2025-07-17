import cv2
import os

# Caminho para o vídeo
video_path = 'test9.mp4'
# Pasta onde os frames serão salvos
output_folder = 'frames_extraidos'
# Intervalo entre os frames que serão salvos (ex: a cada 10 frames)
frame_interval = 400

# Cria a pasta se ela não existir
os.makedirs(output_folder, exist_ok=True)

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Salva frame a cada "frame_interval" frames
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_folder, f'frame_{saved_count:05d}.jpg')
        cv2.imwrite(frame_filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f'{saved_count} frames salvos em: {output_folder}')
