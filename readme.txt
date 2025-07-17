1. Grava o video
2. renomeia o "video_path" de frames.py para usar o nome do video
3. roda o frames.py
4. roda o labelimg: labelImg C:\Users\Luan\workspace\visao_comp\frames_extraidos C:\Users\Luan\workspace\visao_comp\classes.txt
5. deixa todo os arquivos dentro da pasta "frames_extraidos", tanto .png quanto .txt
6. roda o imagem_alb.py
7. troca os dados de dataset pelos os dados de dataset_aug
8. roda o train.py

obs: 
1. precisa saber qual placa de video tem:
cmd > nvidia-smi
1.2. dependendo da placa de video instalar:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
1.3. para saber se ta tudo ok rodar:
>>> import torch
>>> print(torch.cuda.is_available())
True
>>> print(torch.cuda.get_device_name(0))
NVIDIA GeForce GTX 1660 SUPER

2. feito usando python 3.9 (labelimg não buga)