# Lista completa de nombres
nombres = [
    'Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 
    'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes'
]

# Definir los nombres de magos, científicos y otros
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos + cientificos]

# Función para hacer grandiosos a los magos
def hacer_grandioso(lista_magos):
    return [f"El gran {mago}" for mago in lista_magos]

# Función para imprimir nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


print("Lista completa sin modificar:")
imprimir_nombres(nombres)

magos_grandiosos = hacer_grandioso(magos)

print("\nMagos grandiosos:")
imprimir_nombres(magos_grandiosos)

print("\nCientíficos:")
imprimir_nombres(cientificos)

print("\nOtros:")
imprimir_nombres(otros)
