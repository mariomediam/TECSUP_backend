from camelcase import CamelCase

instancia = CamelCase("alumnos")

testo ="hola alumnos este es una prueba"
resultado = instancia.hump(testo)

print(resultado)