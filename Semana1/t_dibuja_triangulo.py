# ----------------- DIBUJA TRIANGULO ------------------

altura = int(input("Ingrese altura: "))

def tiangulo_invertido(altura):
    for i in range(altura):  
        nroAsteriscos = altura - i
        print("*"*nroAsteriscos)

tiangulo_invertido(altura)
