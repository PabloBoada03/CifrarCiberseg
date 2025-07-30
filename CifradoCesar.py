#Se ingresa el mensaje
entrada = input("Ingrese el texto a cifrar: ")
#Se ingresa la llave (desplazamiento)
llave = int(input("Ingrese la llave: "))

entrada_letraxletra= []
#Se separa el string en letras individuales
for i in range(entrada.__len__()):
    entrada_letraxletra.append(entrada[i])

entrada_ascii= []
#Se convierte cada caracter a su código ASCII
for i in range(entrada_letraxletra.__len__()):
    entrada_ascii.append(ord(entrada_letraxletra[i]))

cifrado = []

for i in range(entrada_ascii.__len__()):
    if entrada_ascii[i] != 32:
        if 65 <= entrada_ascii[i] <= 90: #<--- estas serían las mayúsculas
            #1. restamos 65 para que la 'A' sea el 0 del alfabeto
            #2. Sumamos la llave
            #3. Usamos % 26 para que regrese al inicio si se pasa de la 'Z'
            #4. volvemos a sumar el 65 para volver al rango ASCII original
            nueva_letra = ((entrada_ascii[i] - 65 + llave) % 26 ) + 65
        elif 97 <= entrada_ascii[i] <= 122: #<--- Estas serían las minúsculas
            #1. restamos 97 para que la 'a' sea el 0 del alfabeto
            #2. Sumamos la llave
            #3. Usamos % 26 para que regrese al inicio si se pasa de la 'z'
            #4. volvemos a sumar el 97 para volver al rango ASCII original
            nueva_letra = ((entrada_ascii[i] - 97 + llave) % 26) + 97
        else:
            nueva_letra = entrada_ascii[i] #No se cifran (signos, símbolos, etc)

        cifrado.append(chr(nueva_letra))
    else:
        cifrado.append(' ')

        

print("Texto cifrado: " + ''.join(cifrado)) #imprimir el arreglo como una frase no separada por comas


