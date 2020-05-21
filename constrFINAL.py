
import cv2
import numpy as np
import os

def constrast_streching(folder, filename):


    full_filename = os.path.join(folder, filename)#importante
    res= cv2.imread(full_filename)#importante
    imagen_original = cv2.imread(full_filename , cv2.IMREAD_GRAYSCALE)
    #Detallamos los valores de las variables de Contrast stretching 
    a = 0   # límite inferior
    b = 255 # límite superior
    #c = 69
    #d = 149
    c = np.min(imagen_original)  # El menor valor de los pixeles
    d = np.max(imagen_original)  # El mayor valor de los pixeles

    #porcentaje=5

    

    longi=d-c   #calculamos la longitud del rango
    limitec=(longi*5)/100 #calculamos el limite a partir del porcentaje
            

    newc=c-limitec# El menor valor  en un limite de 5% 

    limited=(longi*5)/100 #calculamos el limite a partir del porcentaje
    newd=d+limited# El menor valor en un limite de 95%



    #print("estos son")

    #print(newc,newd)
    alto, ancho, canales = imagen_original.shape 
    #c,d= limite(histOut,alto*ancho,5)
    #print(c,d)
    #print(min,max)



    for x in range(alto):
        for y in range(ancho):
            #re = point_operatorOutlier(Outlier[x][y])#aplicamos el operador punto 
            re = (Outlier[x][y]-newc) * ((b-a)/(newd -newc)+a)
            if(re<0):
                res[x][y]=0  
            elif(re>255):
                res[x][y]=255
            else:
                res[x][y]=re
           
    #hisRes = cv2.calcHist([res], [0], None, [256], [0, 256])
    #cv2.imshow('Resultado',res)        
    cv2.imwrite('res.jpg',res)#Guardamos la imagen resultante        


    #plt.plot(histOut, color='red' )
    #plt.plot(histOriginal, color = 'black')
    #plt.plot(hisRes, color='green')
    #plt.xlabel('Intensidad de iluminacion')
    #plt.ylabel('Cantidad de pixeles')
    #plt.show()



    img_result = res #importante
    full_filename_new = os.path.join(folder, 'constraint' + filename) #importante
    cv2.imwrite(full_filename_new, img_result) #importante

    return full_filename_new #importante

operador_raiz('./img/' , 'contr2.jpg')


