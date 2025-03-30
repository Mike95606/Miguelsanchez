contador="si"
while contador=="si":
    
    print ("robot c3po", "escribe una palabra valida")
    palabra=input()
    if palabra=="hola":
        print("hola humano mediocre")
        print("quieres seguir interactuando")
        contador=input()
    elif palabra=="adios":
        print("adios terricola")
        print("quieres seguir interactuando")
        contador=input()
    else:
        print("instruccion no reconocida")
        print("quieres seguir interactuando")
        contador=input()
