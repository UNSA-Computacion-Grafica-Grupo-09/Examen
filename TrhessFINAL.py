import cv2
import numpy as np
from matplotlib import pyplot as plt

def Thresholding(folder, filename):

	full_filename = os.path.join(folder, filename)#importante
    res= cv2.imread(full_filename)#importante
    img= cv2.imread(full_filename , cv2.IMREAD_GRAYSCALE)

	#img = cv2.imread('thresh2.jpg')
	#gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	#neg=255-gray
	#img = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
	#cv2.imshow('thresh2', img)
	#cv2.imshow('gray', gray)
	#cv2.imshow('neg',neg)




	h, w = img.shape
	res = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)

	for i in range(h):
	    for j in range(w):
	        if(img[i][j]<=170):
	            res[i][j]=255
	        else:
	            res[i][j]=0

	#cv2.imshow('Sin celulas saludables',gray)


	img_result = res #importante
	full_filename_new = os.path.join(folder, 'Thresholding' + filename) #importante
	cv2.imwrite(full_filename_new, img_result) #importante

	return full_filename_new #importante

operador_raiz('./img/' , 'thresh2.jpg')

 