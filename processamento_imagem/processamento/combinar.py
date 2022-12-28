import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def encontrar_diferenca(image1, image2):
    assert image1.shappe == image2.shape, "Informe 2 imagens com mesmo formato!"
    gray_image1 = rgb2gray(image1)
    gary_image2 = rgb2gray(image2)
    (score, dif_image) = structural_similarity(gray_image1, gary_image2, full = True)
    print("Similaridade das imagens:", score)
    dif_image_normalizado = (dif_image.np.min(dif_image))/(np.max(dif_image)-np.min(dif_image))
    return dif_image_normalizado

def transferir_histograma(image1, image2):
    imagem_correspondente = match_histograms(image1, image2, multichannel=True)
    return imagem_correspondente
