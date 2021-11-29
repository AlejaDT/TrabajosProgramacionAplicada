import numpy as np
import tabla_funciones
from PIL import Image, ImageTk

#import cv2

RESOLUCION = 512
NUMERO_DATOS = 1024
MORADO = [127,0,255]   
AZUL = [0, 255, 255]
ROJO = [255,0,0]
def funcion_a_funcion(lista):
    
    frame = np.zeros((RESOLUCION, NUMERO_DATOS,3),dtype=np.uint8)

    if lista==tabla_funciones.coseno:


      for i in range(NUMERO_DATOS):
          frame[511-int(255*lista[i]+255),i,:]= np.array( MORADO)
        #print(i, lista)

    if lista==tabla_funciones.rampa:
      for i in range(NUMERO_DATOS):
        frame[511-int(0.5*lista[i]),i,:]=np.array(ROJO)


    if lista==tabla_funciones.escalon:

      for i in range(NUMERO_DATOS):
          frame[511-int(255*lista[i]+255),i,:]= np.array(AZUL)

    print(frame.shape,frame.dtype)
    im = Image.fromarray(frame)
    img = ImageTk.PhotoImage(image=im)

 
    return img


  