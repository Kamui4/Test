import sys
from Librerias.clases import *
import tkinter
from PIL import ImageTk, Image
import ctypes
from Librerias.metodos import adiosmclovin
import os
def resource_path(relative_path): #sirve para integrar la carpeta images en el .exe
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Main(root)
    #icono
    myappid = 'ddxdxdxd'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap(resource_path("mclovin.ico"))
    #estado de mclovin
    estado = {"imagen_actual": 1}
    #Primera foto
    mclovin = Image.open(resource_path("mclovin.jpg"))
    mclovin = mclovin.resize((400, 400))
    mclovin = ImageTk.PhotoImage(mclovin)
    #Segunda foto
    carnet = Image.open(resource_path("carnet.jpg"))
    carnet = carnet.resize((400, 400))
    carnet = ImageTk.PhotoImage(carnet)

    etiqueta = tkinter.Label(root, text="Tonto el que lo lea",font=("Arial",20),background="LightGray")
    etiqueta.pack()
    boton = tkinter.Button(root, image=mclovin, command=lambda:adiosmclovin(boton,mclovin,carnet,estado))
    #boton.config(height=420,width=420)
    boton.pack()
    boton.image = carnet
    tkinter.Button(root, text="Cerrar la Ventana",font=("Arial",12),background="LightGray", command=root.quit).pack()
    root.mainloop()