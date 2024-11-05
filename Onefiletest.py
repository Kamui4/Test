import tkinter
from PIL import ImageTk, Image
import ctypes

class Main:
    def __init__(self,root):
        self.root = root
        self.root.title("Mclovin")
        self.root.geometry("500x500")
        #self.root.resizable(False,False)
        self.root.config(background="#1e1f22") ##c2f5dd

def adiosmclovin(boton,mclovin,carnet,estado):
    if estado["imagen_actual"]==1:
        boton.config(image=carnet)
        boton.image = carnet
        estado["imagen_actual"] = 2
    else:
        boton.config(image=mclovin)
        boton.image = mclovin
        estado["imagen_actual"] = 1
if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Main(root)
    #icono
    myappid = 'ddxdxdxd'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
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