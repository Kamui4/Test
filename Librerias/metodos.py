def adiosmclovin(boton,mclovin,carnet,estado):
    if estado["imagen_actual"]==1:
        boton.config(image=carnet)
        boton.image = carnet
        estado["imagen_actual"] = 2
    else:
        boton.config(image=mclovin)
        boton.image = mclovin
        estado["imagen_actual"] = 1
