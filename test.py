import cv2
from ultralytics import YOLO
import os

# === CONFIGURAÇÕES ===
MODEL_PATH = r'C:\Users\TI DEV\visao_compt\visao-computacional\runs\detect\v2\weights\best.pt'
VIDEO_PATH = 'teste_mp4.mp4'
CONF_THRES = 0.25
IOU_THRES = 0.45
IMGSZ = 896
REGION_X_START = 0
REGION_Y_START = 0
DEBUG = True

# === FUNÇÕES AUXILIARES ===
def draw_detections(frame, boxes, confidences, classes, names, x_start, y_start):
    
    for box, conf, cls in zip(boxes, confidences, classes):
        conf = float(conf)
        cls = int(cls)

        x1, y1, x2, y2 = box.cpu().numpy()
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

        # Verifica se a detecção está na região de interesse
        if cx < x_start or cy < y_start:
            continue

        label = f"{names[cls]} {conf:.2f}"
        color = (0, 255, 0) if conf >= 0.80 else (0, 0, 255)

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

def process_video():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em: {MODEL_PATH}")

    model = YOLO(MODEL_PATH)
    names = model.names

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        raise IOError(f"Erro ao abrir vídeo: {VIDEO_PATH}")

    ret, tmp = cap.read()
    if not ret:
        raise RuntimeError("Não foi possível ler o primeiro frame do vídeo.")

    h, w = tmp.shape[:2]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=CONF_THRES, iou=IOU_THRES, imgsz=IMGSZ)[0]

        draw_detections(frame, results.boxes.xyxy, results.boxes.conf,
                        results.boxes.cls, names, REGION_X_START, REGION_Y_START)

        # Linhas de referência (opcional)
        cv2.line(frame, (0, REGION_Y_START), (w, REGION_Y_START), (255, 255, 0), 1)
        cv2.line(frame, (REGION_X_START, 0), (REGION_X_START, h), (255, 255, 0), 1)

        cv2.imshow('Detecções', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

# === EXECUÇÃO PRINCIPAL ===
if __name__ == "__main__":
    process_video()
