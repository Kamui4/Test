from Librerias.clases import *
import tkinter
from PIL import ImageTk, Image
import ctypes
from Librerias.metodos import adiosmclovin
if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Main(root)
    #icono
    mcicon = "XD"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(mcicon)
    root.iconbitmap("images/mclovin.ico")
    #estado de mclovin
    estado = {"imagen_actual": 1}
    #Primera foto
    mclovin = Image.open("images/mclovin.jpg")
    mclovin = mclovin.resize((400, 400))
    mclovin = ImageTk.PhotoImage(mclovin)
    #Segunda foto
    carnet = Image.open("images/carnet.jpg")
    carnet = carnet.resize((400, 400))
    carnet = ImageTk.PhotoImage(carnet)

    etiqueta = tkinter.Label(root, text="Tonto el que lo lea",font=("Arial",20),background="LightGray")
    etiqueta.pack()
    boton = tkinter.Button(root, image=mclovin, command=lambda:adiosmclovin(boton,mclovin,carnet,estado))
    boton.pack()
    boton.image = carnet
    tkinter.Button(root, text="Cerrar la Ventana",font=("Arial",12),background="LightGray", command=root.quit).pack()
    root.mainloop()