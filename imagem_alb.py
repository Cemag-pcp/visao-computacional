import os
import cv2
import shutil
import random
from glob import glob
import albumentations as A
from sklearn.model_selection import train_test_split

# Configurações
INPUT_DIR = 'frames_extraidos'
AUG_DIR = 'dataset_aug'
N_VARIACOES = 5
IMG_EXT = ('.jpg', '.png')

# Cria estrutura de pastas
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(AUG_DIR, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(AUG_DIR, 'labels', split), exist_ok=True)

# Transformações de coloração
transform = A.Compose([
    A.RandomBrightnessContrast(p=1.0),
    A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=1.0),
    A.RGBShift(r_shift_limit=20, g_shift_limit=20, b_shift_limit=20, p=1.0),
    A.ToGray(p=0.2),
])

# Carrega imagens e labels
img_paths = [p for p in glob(os.path.join(INPUT_DIR, '*')) if p.endswith(IMG_EXT)]
img_paths.sort()

# Divide base original
train_imgs, temp_imgs = train_test_split(img_paths, test_size=0.2, random_state=42)
val_imgs, test_imgs = train_test_split(temp_imgs, test_size=0.5, random_state=42)

splits = {
    'train': train_imgs,
    'val': val_imgs,
    'test': test_imgs,
}

# Processa cada split
for split, paths in splits.items():
    for img_path in paths:
        filename = os.path.splitext(os.path.basename(img_path))[0]
        label_path = os.path.join(INPUT_DIR, filename + '.txt')
        if not os.path.exists(label_path):
            print(f'Label não encontrado: {label_path}, pulando...')
            continue

        # Copia original
        new_img_name = f'{filename}.jpg'
        shutil.copy(img_path, os.path.join(AUG_DIR, 'images', split, new_img_name))
        shutil.copy(label_path, os.path.join(AUG_DIR, 'labels', split, filename + '.txt'))

        # Gera variações
        img = cv2.imread(img_path)
        for i in range(N_VARIACOES):
            aug_img = transform(image=img)['image']
            aug_filename = f'{filename}_aug{i}.jpg'
            aug_labelname = f'{filename}_aug{i}.txt'

            cv2.imwrite(os.path.join(AUG_DIR, 'images', split, aug_filename), aug_img)
            shutil.copy(label_path, os.path.join(AUG_DIR, 'labels', split, aug_labelname))

print(f"\n✅ Dataset aumentado e dividido em 'train', 'val' e 'test' em: {AUG_DIR}")
