import re


def cifrado_cesar(texto, llave):
    entrada_ascii = [ord(c) for c in texto]
    cifrado = []

    for ascii_val in entrada_ascii:
        if ascii_val != 32:
            if 65 <= ascii_val <= 90:
                nueva_letra = ((ascii_val - 65 + llave) % 26) + 65
            elif 97 <= ascii_val <= 122:
                nueva_letra = ((ascii_val - 97 + llave) % 26) + 97
            else:
                nueva_letra = ascii_val
            cifrado.append(chr(nueva_letra))
        else:
            cifrado.append(' ')
    return ''.join(cifrado)

def cifrado_vigenere(texto, clave):
    clave = clave.lower()
    clave_repetida = ""
    indice_clave = 0
    for c in texto:
        if c != ' ':
            clave_repetida += clave[indice_clave % len(clave)]
            indice_clave += 1
        else:
            clave_repetida += ' '

    cifrado = []
    for i in range(len(texto)):
        if texto[i] != ' ':
            k = ord(clave_repetida[i]) - 97
            if texto[i].isupper():
                nueva_letra = ((ord(texto[i]) - 65 + k) % 26) + 65
            else:
                nueva_letra = ((ord(texto[i]) - 97 + k) % 26) + 97
            cifrado.append(chr(nueva_letra))
        else:
            cifrado.append(' ')
    return ''.join(cifrado)

def descifrar_cesar(texto, clave):
    abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    abecedario_min = abecedario.lower()
    resultado = ''
    for caracter in texto:
        if caracter.upper() in abecedario:
            if caracter.isupper():
                indice = abecedario.find(caracter)
                nuevo_indice = (indice - clave) % len(abecedario)
                resultado += abecedario[nuevo_indice]
            else:
                indice = abecedario_min.find(caracter)
                nuevo_indice = (indice - clave) % len(abecedario_min)
                resultado += abecedario_min[nuevo_indice]
        else:
            resultado += caracter
    return resultado

def fuerza_bruta_cesar(texto):
    print("\nResultados por fuerza bruta:")
    for clave in range(1, 28):
        print(f"Clave {clave:2d}: {descifrar_cesar(texto, clave)}")

def generar_clave_repetida(texto, clave):
    clave = clave.lower()
    clave_repetida = ''
    i = 0
    for char in texto:
        if char != ' ':
            clave_repetida += clave[i % len(clave)]
            i += 1
        else:
            clave_repetida += ' '
    return clave_repetida

def descifrar_vigenere(texto, clave):
    clave_repetida = generar_clave_repetida(texto, clave)
    resultado = []
    for i, c in enumerate(texto):
        if c.isalpha():
            base = 65 if c.isupper() else 97
            k = ord(clave_repetida[i]) - 97
            nueva = chr((ord(c) - base - k + 26) % 26 + base)
            resultado.append(nueva)
        else:
            resultado.append(c)
    return ''.join(resultado)

def contar_tokens_validos(texto):
    COMMON_WORDS_ES = {
        'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para',
        'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este',
        'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta',
        'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni',
        'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'esto', 'mí', 'antes', 'algunos', 'qué',
        'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes',
        'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros',
        'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'mío', 'mía',
        'ciberseguridad', 'importante', 'servidor', 'proteger', 'sistema', 'informacion', 'datos',
        'acceso', 'controlado', 'ataque', 'externo', 'defensa', 'usuario'
    }
    palabras = re.findall(r'\b[a-záéíóúñ]{2,}\b', texto.lower())
    return sum(1 for palabra in palabras if palabra in COMMON_WORDS_ES)

def fuerza_bruta_vigenere(texto):
    try:
        with open("rockyou_3000.txt", "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()

        match = re.search(r'passwords\s*=\s*\[(.*?)\]', contenido, re.DOTALL)
        if not match:
            print("No se encontró la lista 'passwords' en el archivo.")
            return

        passwords = eval("[" + match.group(1) + "]")
        claves_validas = [p for p in passwords if p.isalpha()][:100]

        mejor_puntaje = 0
        mejor_descifrado = ""
        mejor_clave = ""

        for clave in claves_validas:
            intento = descifrar_vigenere(texto, clave)
            tokens = contar_tokens_validos(intento)
            print(f"Clave probada: {clave.ljust(12)} → Tokens: {tokens} → Resultado: {intento}")
            if tokens > mejor_puntaje:
                mejor_puntaje = tokens
                mejor_descifrado = intento
                mejor_clave = clave

        if mejor_puntaje > 0:
            print("\nClave más probable encontrada:", mejor_clave)
            print("Tokens reconocidos:", mejor_puntaje)
            print("Texto descifrado:\n", mejor_descifrado)
        else:
            print("\nNo se encontró una clave válida que produzca texto legible.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'rockyou_3000.txt'.")

# ---------------------------------------
# INTERFAZ DE USUARIO
# ---------------------------------------

def pedir_texto_clave():
    texto = input("Ingrese el texto (solo letras y espacios): ").strip()
    if not all(c.isalpha() or c == ' ' for c in texto):
        print("Error: El mensaje solo puede contener letras y espacios.")
        return None, None
    clave = input("Ingrese la clave (solo letras, opcional para descifrado): ").strip()
    return texto, clave

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Cifrado César")
        print("2. Descifrado César")
        print("3. Cifrado Vigenère")
        print("4. Descifrado Vigenère")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            texto, clave = pedir_texto_clave()
            if texto and clave.isdigit():
                print("Texto cifrado:", cifrado_cesar(texto, int(clave)))
        elif opcion == '2':
            texto = input("Ingrese el texto a descifrar: ")
            clave = input("Ingrese la clave (deje vacío para usar fuerza bruta): ")
            if clave.strip() == '':
                fuerza_bruta_cesar(texto)
            elif clave.isdigit():
                print("Texto descifrado:", descifrar_cesar(texto, int(clave)))
            else:
                print("Clave inválida.")
        elif opcion == '3':
            texto, clave = pedir_texto_clave()
            if texto and clave.isalpha():
                print("Texto cifrado:", cifrado_vigenere(texto, clave))
        elif opcion == '4':
            texto, clave = pedir_texto_clave()
            if texto:
                if clave:
                    if clave.isalpha():
                        print("Texto descifrado:", descifrar_vigenere(texto, clave))
                    else:
                        print("Clave inválida.")
                else:
                    fuerza_bruta_vigenere(texto)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
