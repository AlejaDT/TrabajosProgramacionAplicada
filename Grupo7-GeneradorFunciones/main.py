'''
DOCTYPE:
Generador de funciones Python
Presentado por:
Juan Pablo Patiño Chaux
Alejandra Díaz Tejada

El siguiente programa consiste en 3 rutinas que implementan la creación de funciones, la visualización en el entorno y la interfaz gráfica
'''


import tkinter as tk
from PIL import Image
from PIL import ImageTk
import tabla_funciones
import pantalla

root = tk.Tk()
root.title("GENERADOR DE FUNCIONES")

def cambia_funciones():
    if seleccionada.get() == 1:
      imagen=pantalla.funcion_a_funcion(tabla_funciones.coseno)

    if seleccionada.get() == 2:
      imagen=pantalla.funcion_a_funcion(tabla_funciones.rampa)
      
    if seleccionada.get() == 3:
      imagen=pantalla.funcion_a_funcion(tabla_funciones.escalon)

    monitor.configure(image=imagen)
    monitor.image = imagen


seleccionada = tk.IntVar()#"nada"#IntVar('0')
rb_coseno = tk.Radiobutton(root, text="Coseno", width=45, value=1, variable=seleccionada, command=cambia_funciones)
rb_coseno.grid(column=0, row=0, padx=5, pady=5)
rb_rampa = tk.Radiobutton(root, text="Rampa", width=45, value=2, variable=seleccionada, command=cambia_funciones)
rb_rampa.grid(column=1, row=0, padx=5, pady=5)
rb_escalon = tk.Radiobutton(root, text="Escalon", width=45, value=3, variable=seleccionada, command=cambia_funciones)
rb_escalon.grid(column=2, row=0, padx=5, pady=5)

monitor = tk.Label(root)
monitor.grid(column=0, row=1, columnspan=3)

imagen=pantalla.funcion_a_funcion([255,255,255])
monitor.configure(image=imagen)
monitor.image = imagen

root.mainloop()
  