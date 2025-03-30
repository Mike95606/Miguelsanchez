edad=0
print("introduce tu edad")
edad=input()
edad=int(edad)
if edad>=18 and edad<=21:
    print("puedes entrar pero sin bebidas alcoholicas")
elif edad<18:
        print("lo siento no puedes entrar")
elif edad>21:
        print("bienvenido")
else:
    print("error")

        
