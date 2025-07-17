from ultralytics import YOLO
import os
import multiprocessing

# Caminho absoluto da raiz do projeto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
  data_path = os.path.join(ROOT_DIR, 'datasets', 'dataset', 'data.yaml')
  model = YOLO('yolov5s.pt')
  model.train(
    data=data_path,
    epochs=30,
    imgsz=896,
    batch=4,
    name='v1'
  )

if __name__ == '__main__':
  multiprocessing.freeze_support()
  main()