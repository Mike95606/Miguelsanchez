print("desea evaluar un numero? si/no");
respuesta=input();
print("introduce un numero entero _");
numero=input();
int_numero=int(numero);
while respuesta == "si":
    if int_numero > 0:
        print(numero+" el numero es positivo")
        print(numero+" desea evaluar otro numero si/no")
        respuesta=input()
        print("introduce un numero____")
        numero=input()
        int_numero=int(numero)

    elif int_numero < 0:
           print(numero+" el numero es negativo")
           print(numero+" desea evaluar otro numero si/no")
           respuesta=input()
           print("introduce un numero____")
           numero=input()
           int_numero=int(numero)
           

            
    elif int_numero == 0:
            print("el numero es 0")
            print("desea evaluar otro numero si/no")
            respuesta=input();
            print("introduce un numero__")
            numero=input()
            int_numero=int(numero)
            
        
