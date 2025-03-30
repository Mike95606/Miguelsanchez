
salir="no"
while salir=="no":
    print("Este es el convertidor de edad de tu mascota")
    print("introduce la edad humana que tiene tu mascota")
    edad=input()
    edad=int(edad)
    print("Es perro o gato?")
    mascota=input()
    if mascota =="perro":
        edad=edad*7
        print(edad)
        print("desea salir si/no)")
        salir=input()
    elif mascota =="gato":
        edad=edad*5
        print(edad)
        print("desea salir si/no)")
        salir=input()
    else:
        print("error en el dato")
        print("desea salir si/no)")
        salir=input()
