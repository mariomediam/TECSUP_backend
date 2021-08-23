numero_adivinar = 10

numeroIngresado = 0

while numeroIngresado != numero_adivinar:
    numeroIngresado = int(input("Ingresa número"))
    if numeroIngresado > numero_adivinar:
        print("El número es menor que ese")
    elif (numeroIngresado < numero_adivinar):
        print("El número es mayor que ese")

print("Advinaste el número!!!!")