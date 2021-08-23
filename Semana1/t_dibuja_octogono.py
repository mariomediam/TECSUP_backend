# ----------------- DIBUJA OCTOGONO ------------------


longitud = int(input("Ingrese longitud: "))

def dibujar_octogono(longitud):
    nroAsteriscos = longitud
    espaciosBlanco = longitud - 1

    while espaciosBlanco > 0:    
        print(" "*espaciosBlanco , end="")
        print("*"*nroAsteriscos, end="")
        print(" "*espaciosBlanco)
        nroAsteriscos += 2
        espaciosBlanco -= 1

    for i in range(longitud-1):
        print("*"*nroAsteriscos)
        
    while nroAsteriscos >= longitud:   

        #print(" "*espaciosBlanco , end="")
        #print("*"*nroAsteriscos, end="")
        #print(" "*espaciosBlanco)
        print(f"{" "*espaciosBlanco}")
        nroAsteriscos -= 2
        espaciosBlanco += 1


dibujar_octogono(longitud)


for i in "AMIGO":
    print(f"Dame una {i*3}")
print("¡AMIGO!")