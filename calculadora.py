print("hola esta es la calculadora de propinas")
print("introduce el costo de la cuenta")
cuenta=input()
cuenta=float(cuenta)
print("introduce que porcentaje de la propina quieres aportar 10, 20, 30")
propina=input()
propina=float(propina)
suma=float(0)

suma1=cuenta*propina
print(suma)
suma3=suma1//100
suma=suma3+cuenta
print(suma)
