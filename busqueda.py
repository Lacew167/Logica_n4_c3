def buscar(dato, arreglo): #dato que vamos a buscar y lista donde lo vamos a buscar
    encontro=False
    i=0
    while i<len(arreglo) and not encontro:
        if arreglo[i]==dato:
            encontro=True
        i=i+1
    return encontro


def buscar_p(dato, arreglo): #dato que vamos a buscar y lista donde lo vamos a buscar
    encontro=False
    i=0
    while i<len(arreglo) and not encontro:
        if arreglo[i]==dato:
            encontro=True
            pos=i
        i=i+1
    return encontro, pos

#modulo donde pregunten al usuario que dato va a buscar
def buscar_dato(correos,arreglo):
    print("Ingrese el correo que quiere buscar")
    dato=input()
    existe,indice=buscar_p(dato, correos)
    if existe:
        print("Ya esta registrado con la posicion {pos}")
    else:
        print("No esta registrado")

#cuerpo principal
nombres=["Jenny","Maria","Fabiana","Tulio","Jesus","Betania"]
correos=['abc', "xyz", "bvnvn","hasd","haipsdh", "correo"]
print("Cual nombre desea consultar?")
nombre=input()
print(buscar(nombre,nombres))
if buscar(nombre, nombres):
    print(f"Se encontro el nombre {nombres}")
else:
    print("No se encontro ese nombre")


