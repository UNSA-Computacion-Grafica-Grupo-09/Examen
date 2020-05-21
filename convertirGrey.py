import cv2
import os


def imagen_gray(folder, filename):
    full_filename = os.path.join(folder, filename)
    imagenes = cv2.imread(full_filename)
    imagen_gray = cv2.cvtColor(imagenes, cv2.COLOR_BGR2GRAY)
    full_filename_new = os.path.join(folder, 'Resultado' + filename)
    cv2.imwrite(full_filename_new, imagen_gray)

    return full_filename_new