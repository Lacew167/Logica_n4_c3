def cargar(arreglo,arreglo2,arreglo3):
    resp=""
    while resp.lower()!="n":
        print("ingrese el nombre de la persona")
        dato=input()
        arreglo.append(dato) #guardamos el nombre de la persona
        print("ingrese el sexo de la persona F/M")
        sexo=input()
        arreglo2.append(sexo)
        print(f"Cuantos anos tienes {dato}")
        dato3=int(input())
        arreglo3.append(dato3)
        resp=input("presione n para detener la carga")
        if resp.upper()=="N":
            break

def promediar(arreglo):
    acumulador=0
    for valor in arreglo:
        acumulador=acumulador+valor
    prom=acumulador/len(arreglo)
    return prom

def listar(arreglo, arreglo2, arreglo3,  valor):#valor a comparar, 2 valor a comparar, valor a mostrar
    for i in range(len(arreglo)):
        if arreglo[i]>valor and arreglo2[i].upper()=="F":
            print(arreglo3[i])



    print("---------------------")

print("Chicas con edad mayor al promedio")
    #for iterar sobre arreglo edades
    #comparar la edad
    #imprimir el nombre de la posicion


#cuerpo principal
nombres=[]
generos=[]
edades=[]
cargar(nombres, generos, edades)
promedio_edades=promediar(edades)
print(edades)
print(f"EL promedio de edades es {promedio_edades}")
listar(edades, generos, nombres,promedio_edades)