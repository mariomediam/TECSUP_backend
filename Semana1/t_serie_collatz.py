# ----------------- SERIE COLLATZ ------------------

numero = int(input("Ingrese número: "))

def serie_collatz(numero):    
    while numero != 1:
        if numero % 2 == 0:
            numero = numero / 2
        else:
            numero = numero * 3 + 1
        print(numero, end=", ")

serie_collatz(numero)

for i in "AMIGO":
    print(f"Dame una {i*3}")
print("¡AMIGO!")