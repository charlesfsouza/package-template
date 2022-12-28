from skimage.transform import resize

def redimensionar_imagem(image, proporcao):
    assert 0 <= proporcao <= 1, "Informe uma proporção entre 0 e 1!"
    height = round(image.shape[0] * proporcao)
    width = round(image.shape[1] * proporcao)
    imagem_redimensionada = resize(imagem, (height, width), anti_aliasing=True)
    return imagem_redimensionada