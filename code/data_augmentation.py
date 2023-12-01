import os
import imageio
import numpy as np
from skimage import color, exposure, img_as_ubyte

def apply_brightness_augmentation(input_path, output_path):
    # Certifique-se de que o diretório de saída existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Liste todos os arquivos no diretório de entrada
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.png', '.jpeg','.bmp'))]

    # Loop através de cada imagem
    for img_file in image_files:
        img_path = os.path.join(input_path, img_file)

        # Carregue a imagem usando imageio
        img = imageio.imread(img_path)

        # Ajuste o brilho usando skimage
        bright_img = exposure.adjust_gamma(img, gamma=0.6)

        # Salve a imagem com brilho aumentado na pasta de saída
        imageio.imsave(os.path.join(output_path, f"{img_file[:-5]}_brightness_aug.png"), img_as_ubyte(bright_img))

def apply_saturation_augmentation(input_path, output_path):
    # Certifique-se de que o diretório de saída existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Liste todos os arquivos no diretório de entrada
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.png', '.jpeg','.bmp'))]

    # Loop através de cada imagem com brilho ajustado
    for img_file in image_files:
        img_path = os.path.join(input_path, img_file)

        # Carregue a imagem usando imageio
        img = imageio.imread(img_path)

        # Converta a imagem para HSV usando skimage
        hsv = color.rgb2hsv(img)

        # Ajuste a saturação
        hsv[:, :, 1] = hsv[:, :, 1] * 1.5  # Valor maior para aumentar a saturação

        # Converta de volta para RGB
        img_saturated = color.hsv2rgb(hsv)

        # Salve a imagem saturada na pasta de saída
        imageio.imsave(os.path.join(output_path, f"{img_file[:-5]}_saturated_aug.png"), img_as_ubyte(img_saturated))

# Exemplo de uso
input_folder = "/content/dataset"
output_folder = "/content/output"

# Aplica a alteração de brilho
apply_brightness_augmentation(input_folder, output_folder)

# Aplica a alteração de saturação
apply_saturation_augmentation(input_folder, output_folder)
