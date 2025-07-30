entrada = input("Ingrese el texto a descifrar: ")

llave_str = input("Ingrese la llave si la tiene (deje vacío si no la sabe): ")

#Función que descifra el texto con una clave específica
def descifrar_cesar(texto, clave):
    abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'       # Abecedario en español con la Ñ
    abecedario_min = abecedario.lower()              # Abecedario en minúsculas
    resultado = ''                                   

    for caracter in texto:                           
        if caracter.upper() in abecedario:           # Si es una letra (mayúscula o minúscula) que está en el abecedario
            if caracter.isupper():                   # Si la letra es mayúscula
                indice = abecedario.find(caracter)   # Buscamos su posición
                nuevo_indice = (indice - clave) % len(abecedario)  # Movemos hacia atrás (descifrado)
                resultado += abecedario[nuevo_indice]  # Agregamos la nueva letra
            else:                                    # Si la letra es minúscula
                indice = abecedario_min.find(caracter)
                nuevo_indice = (indice - clave) % len(abecedario_min)
                resultado += abecedario_min[nuevo_indice]
        else:
            resultado += caracter  # Si no es letra (espacio, coma, tilde, etc.), se mantiene igual

    return resultado  # Devuelve el mensaje ya descifrado

#Función que prueba todas las posibles claves del 1 al 27 (fuerza bruta)
def fuerza_bruta_cesar(texto):
    print("\n Resultados por fuerza bruta:")
    for clave in range(1, 28):  # Intenta con todas las claves posibles
        print(f"Clave {clave:2d}: {descifrar_cesar(texto, clave)}")

# Aquí se evalúa si el usuario ingresó una clave o no
if llave_str.strip() == '':
    # Si no escribió nada, se ejecuta la fuerza bruta
    fuerza_bruta_cesar(entrada)
else:
    try:
        # Si ingresó algo, intentamos convertirlo a número
        llave = int(llave_str)
        # Se descifra el mensaje usando la clave proporcionada
        resultado = descifrar_cesar(entrada, llave)
        print("\n Mensaje descifrado:", resultado)
    except ValueError:
        # Si la conversión a número falla (por ejemplo, escribió letras), se muestra un error
        print("Error: la llave ingresada no es un número válido.")
