1. Grava o video
2. renomeia o "video_path" de frames.py para usar o nome do video
3. roda o frames.py
4. roda o labelimg: labelImg C:\Users\pcp2\visao\visao-computacional\frames_extraidos C:\Users\pcp2\visao\visao-computacional\classes.txt
C:\Users\pcp2\visao\visao-computacional\frames_extraidos
C:\Users\pcp2\visao\visao-computacional\classes.txt

5. deixa todo os arquivos dentro da pasta "frames_extraidos", tanto .png quanto .txt
5.1. Se quiser mudar o nome dos arquivos, usar o arquivo tratar_nome_arquivo.py

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