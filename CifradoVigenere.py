# Se ingresa el mensaje
entrada = input("Ingrese el texto a cifrar: ")
# Se ingresa la clave (solo letras)
clave = input("Ingrese la clave: ")

# Se convierte la clave a minúsculas para trabajar en un mismo rango ASCII
clave = clave.lower()

# Se construye una clave repetida del mismo largo que el mensaje (ignorando espacios)
clave_repetida = ""
indice_clave = 0
for i in range(len(entrada)):
    if entrada[i] != ' ':
        clave_repetida += clave[indice_clave % len(clave)]
        indice_clave += 1
    else:
        clave_repetida += ' '  # Se conserva el espacio en la clave repetida

cifrado = []

# Recorremos cada carácter del mensaje
for i in range(len(entrada)):
    if entrada[i] != ' ':
        # Se obtiene el desplazamiento desde la clave
        k = ord(clave_repetida[i]) - 97  # 'a' = 0, 'b' = 1, ..., 'z' = 25

        # Si es una letra mayúscula
        if 65 <= ord(entrada[i]) <= 90:
            #1. Restamos 65 para que 'A' sea 0
            #2. Sumamos el desplazamiento 'k'
            #3. Usamos %26 para mantenernos dentro del alfabeto
            #4. Sumamos 65 para regresar al rango ASCII original
            nueva_letra = ((ord(entrada[i]) - 65 + k) % 26) + 65
        # Si es una letra minúscula
        elif 97 <= ord(entrada[i]) <= 122:
            #1. Restamos 97 para que 'a' sea 0
            #2. Sumamos el desplazamiento 'k'
            #3. Usamos %26 para mantenernos dentro del alfabeto
            #4. Sumamos 97 para regresar al rango ASCII original
            nueva_letra = ((ord(entrada[i]) - 97 + k) % 26) + 97
        else:
            nueva_letra = ord(entrada[i])  # No se cifran signos, números, etc.

        # Se agrega el carácter cifrado a la lista
        cifrado.append(chr(nueva_letra))
    else:
        cifrado.append(' ')  # Se conserva el espacio

# Se imprime el arreglo como una frase, sin comas
print("Texto cifrado: " + ''.join(cifrado))
