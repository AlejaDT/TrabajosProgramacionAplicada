# Requerimientos básicos:
# Realizar la simulación de la variación interactiva del volumen de un tanque de agua. 
# Hay que visualizar el tanque y su volumen actual. 
# Además, en una gráfica, visualizar el histórico de los volúmenes.


import tkinter as tk
import time,math


# # Constantes
# ## Dimensiones del Canvas
width=600
height=600

# # Ventana y componentes con tkinter

master = tk.Tk()
master.title ("CONTROL DE TANQUE")
#Deslizador de llenado
deslizador1 = tk.Scale(master, from_=0, to=10, length=200,tickinterval=1, orient=tk.HORIZONTAL)
deslizador1.pack()
#Deslizzador de vaciado
deslizador2 = tk.Scale(master, from_=-10, to=0, length=200,tickinterval=1, orient=tk.HORIZONTAL)
deslizador2.pack()
canvas = tk.Canvas(master, width=width, height=height)
canvas.pack()
img = tk.PhotoImage(file="planta.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)



# ############### INICIO TANQUE
# # Este bloque agrupa la funcionalidad del tanque
# # es candidato para ser convertido en una clase en la siguiente versión 

# #Dimensiones del tanque


capacidad_total, capacidad_actual =100, 30,

# #Ubicación en el canvas en pixeles
izquierda, abajo, derecha, arriba = 155, 300, 325, 200

# #Calcula los pixeles del borde del liquido
alto = abajo - arriba
altura_liquido = int(alto * capacidad_actual /capacidad_total)

#Define los rectangulos que representan el aire y el líquido
aire = canvas.create_rectangle(
    izquierda, arriba,
    derecha, abajo - altura_liquido,
    fill='white',
)
liquido = canvas.create_rectangle(
    izquierda, abajo - altura_liquido,
    derecha, abajo,
    fill='blue',
)

def deja_salir(t,S2):
    '''
    Entradas
    --------
    t:float; indica el tiempo en segundos transcurrido
    S2:float; indica el area de la válvula que permite el paso del caudal
    Salidas
    -------
    volumen:float; indica el volumen de agua que salió o entro en ese tiempo 
    Descripción 
    ----------
    En caso que el valor de la válvula negativo sale el líquido usando el modelo físico correspondiente 
    En caso que el valor sea positivo entra liquido proporciona a la apertura y al tiempo
    '''
    S1=11 # Área superior del tanque
    H=capacidad_actual/S1 # Altura del líquido

    # según http://www.sc.ehu.es/sbweb/fisica3/fluidos/vaciado/vaciado.html
    #h=(sqrt(H)-S2*sqrt(2*9.8/(S1^2-S2^2))*t/2).^2;
    
    h=(math.sqrt(H)-S2*math.sqrt(2*9.8/(S1**2-S2**2))*t/2)**2
    volumen=(H-h)*S1


    if (capacidad_actual-volumen)<0:
            volumen=capacidad_actual
    return volumen

def actualiza_nivel():
        # Ejercicio realizar los comentarios de esta rutina
        '''
        Entradas
        ----------
        alto: float: Limite borde superior del tanque, depende de la capacidad_actual
        capacidad_actual: float: Varia de acuerdo a la regulación de las válvulas mediante el deslizador1 y el desalizador2
        capacidad_total: float: Indica a cuanto está el tanque de llenarse o qué tan vacío está respectivamente

        Salidas
        ---------
        altura_liquido: float: Mediante esta variable se controla la altura del líquido y se emplea como parámetro para el dibujo de líquido en el tanque

        label_volumen: str: Permite visualizar las variaciones en el tiempo del nivel del tanque

        Descripción
        La variación se da de manera exponecial de modo que la actualización del nivel, es decir, el gráfico mediante el cual se representa el líquido y el aire mediante recuadros de canvas
        ----------



        '''

        altura_liquido = int(alto * capacidad_actual / capacidad_total)
        # Dibuja un rectángulo para representar la parte ocupada 
        # y otro para el resto
        canvas.coords(
            aire,
            izquierda, arriba,
            derecha, abajo - altura_liquido,
        )
        canvas.coords(
            liquido,
            izquierda, abajo - altura_liquido,
            derecha, abajo,
        )

label_volumen = tk.Label(canvas, text=capacidad_actual)
label_volumen.place(x=0, y=200)

# #################### FIN TANQUE



tiempo_global= time.time()
label_tiempo = tk.Label(canvas, text=tiempo_global)
label_tiempo.place(x=0, y=0)
def actualizacion_periodica():
        global tiempo_global,capacidad_actual
        label_tiempo.after(100, actualizacion_periodica) #= tk.Label(text=time.time())
        tiempo_actual = time.time()
        label_tiempo['text'] =  str(tiempo_actual)
        tiempo = tiempo_actual - tiempo_global
        tiempo_global = tiempo_actual
        # 

        
        
        S2=deslizador2.get()
        if S2<0:
            capacidad_actual += deja_salir(tiempo,S2)
        else:
            S2=deslizador1.get()
            if S2>0 and  capacidad_actual<100:
              capacidad_actual += tiempo*S2*1
        label_volumen['text'] =  str(capacidad_actual)
        actualiza_nivel()
            


label_tiempo.after(100, actualizacion_periodica)

tk.mainloop()

# #Recomendaciones
# # No se puede usar el mismo deslizador para el líquido que entra y el que sale
# #    Un deslizador para el líquido que entra
# #    Otro deslizador para el líquido que sale
# # El volumen del líquido no puede superar el volumen del tanque
# # Comentar la rutina que le falta el comentario
# # Crear una clase (`class`) para el tanque
# # Además, en una gráfica, visualizar el histórico de los volúmenes.