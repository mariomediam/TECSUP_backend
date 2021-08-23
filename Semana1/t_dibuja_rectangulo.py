# ----------------- DIBUJA RECTANGULO ------------------
altura = int(input("Ingrese altura: "))
ancho = int(input("Ingrese ancho: "))

def dibujar_rectangulo(altura, ancho):
    for i in range(altura):
        print("*"*ancho)


dibujar_rectangulo(altura, ancho)