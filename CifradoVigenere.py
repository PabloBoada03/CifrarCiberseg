# Se ingresa el mensaje
entrada = input("Ingrese el texto a cifrar (solo letras y espacios): ")

# Validación: solo letras y espacios
if not all(c.isalpha() or c == ' ' for c in entrada):
    print("❌ Error: El mensaje solo puede contener letras y espacios.")
    exit()

# Se ingresa la clave (solo letras)
clave = input("Ingrese la clave (solo letras): ")

# Validación: solo letras
if not clave.isalpha():
    print("❌ Error: La clave solo puede contener letras (sin espacios, números ni símbolos).")
    exit()

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

        if entrada[i].isupper():
            nueva_letra = ((ord(entrada[i]) - 65 + k) % 26) + 65
        else:
            nueva_letra = ((ord(entrada[i]) - 97 + k) % 26) + 97

        cifrado.append(chr(nueva_letra))
    else:
        cifrado.append(' ')  # Se conserva el espacio

# Se imprime el resultado como una frase sin comas
print("Texto cifrado: " + ''.join(cifrado))
