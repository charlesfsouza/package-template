from skimage.io import imread, imsave

def ler_imagem(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def salvar_image(image, path):
    imsave(path, image)