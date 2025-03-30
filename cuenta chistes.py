import random
print("esta es la maquina de chistes")
print("presiona enter para contarte un chiste")
respuesta="si"

input()


while respuesta=="si":
    chiste=random.choice(["Doctor, ¿tendré cura?: Por supuesto, cura, misa y funeral","Un niño vuelve a su casa después del colegio. - Mamá, ¿por qué huele tan mal?, mamá, mamá...","¿Cuál es la clave de tu WIfi? Tener dinero y pagarlo.","¿Cuál es el café más peligroso del mundo? El ex-preso","Soy Rosa: Ah, perdóname, es que soy daltónico."])
    print(chiste)
    print("quieres que te cuente otro chiste si no")
    respuesta=input()

    

    
