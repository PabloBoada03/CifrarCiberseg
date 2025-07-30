import re  # Importa módulo de expresiones regulares para análisis de texto

# DICCIONARIO DE PALABRAS COMUNES PARA EVALUAR SI UN TEXTO ES LEGIBLE EN ESPAÑOL 
COMMON_WORDS_ES = {
    'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para',
    'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este',
    'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta',
    'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni',
    'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'esto', 'mí', 'antes', 'algunos', 'qué',
    'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes',
    'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros',
    'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'mío', 'mía'
}

# Añade términos de ciberseguridad al conjunto de palabras comunes
COMMON_WORDS_ES.update({
    'ciberseguridad', 'importante', 'servidor', 'proteger',
    'sistema', 'informacion', 'datos', 'acceso', 'controlado',
    'ataque', 'externo', 'defensa', 'usuario'
})

# GENERA UNA CLAVE REPETIDA QUE IGUALE LA LONGITUD DEL TEXTO CIFRADO 
def generar_clave_repetida(texto, clave):
    clave = clave.lower()
    clave_repetida = ''
    i = 0
    for char in texto:
        if char != ' ':
            clave_repetida += clave[i % len(clave)]
            i += 1
        else:
            clave_repetida += ' '  # Mantiene los espacios donde estaban
    return clave_repetida

# FUNCION DE DESCIFRADO VIGENERE USANDO LA CLAVE REPETIDA 
def descifrar_vigenere(texto, clave):
    clave_repetida = generar_clave_repetida(texto, clave)
    resultado = []

    for i, c in enumerate(texto):
        if c.isalpha():  # Solo descifra letras
            base = 65 if c.isupper() else 97  # Base ASCII según mayúscula o minúscula
            k = ord(clave_repetida[i]) - 97  # Desplazamiento según letra de clave
            nueva = chr((ord(c) - base - k + 26) % 26 + base)  # Fórmula inversa Vigenère
            resultado.append(nueva)
        else:
            resultado.append(c)  # Mantiene los espacios

    return ''.join(resultado)

# FUNCION PARA CONTAR PALABRAS RECONOCIBLES EN ESPAÑOL EN UN TEXTO 
def contar_tokens_validos(texto):
    palabras = re.findall(r'\b[a-záéíóúñ]{2,}\b', texto.lower())  # Extrae palabras
    return sum(1 for palabra in palabras if palabra in COMMON_WORDS_ES)

# SOLICITA ENTRADA AL USUARIO 
texto_cifrado = input("Ingrese el mensaje cifrado (solo letras y espacios): ").strip()

# MENSAJE SOLO CON LETRAS Y ESPACIOS
if not all(c.isalpha() or c == ' ' for c in texto_cifrado):
    print("❌ Error: El mensaje cifrado solo puede contener letras y espacios.")
    exit()

# Solicita clave (puede ser vacía si se quiere usar ataque por diccionario)
clave_manual = input("Ingrese la clave (deje vacío para usar diccionario): ").strip()

# CLAVE SOLO CON LETRAS (SI SE PROPORCIONA)
if clave_manual and not clave_manual.isalpha():
    print("❌ Error: La clave solo puede contener letras (sin espacios, números ni símbolos).")
    exit()

# SI EL USUARIO INGRESÓ UNA CLAVE MANUAL
if clave_manual:
    descifrado = descifrar_vigenere(texto_cifrado, clave_manual)
    print("\nTexto descifrado con clave proporcionada:")
    print(descifrado)

# SI NO SE PROPORCIONA CLAVE, SE INICIA ATAQUE POR DICCIONARIO 
else:
    try:
        # Abre y lee el archivo que contiene la lista rockyou_3000 (formato Python)
        with open("rockyou_3000.txt", "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()

        # Extrae el contenido de la lista "passwords = [...]"
        match = re.search(r'passwords\s*=\s*\[(.*?)\]', contenido, re.DOTALL)
        if not match:
            print("No se encontró la lista 'passwords' en el archivo.")
            exit()

        # Convierte la cadena extraída en una lista real de Python
        passwords = eval("[" + match.group(1) + "]")

        # Filtra solo claves que contengan letras (sin números ni símbolos), y toma las primeras 100
        claves_validas = [p for p in passwords if p.isalpha()]
        claves_validas = claves_validas[:100]

        mejor_puntaje = 0
        mejor_descifrado = ""
        mejor_clave = ""

        # Prueba cada clave válida y evalúa cuántas palabras reconocidas genera
        for clave in claves_validas:
            intento = descifrar_vigenere(texto_cifrado, clave)
            tokens = contar_tokens_validos(intento)
            print(f"Clave probada: {clave.ljust(12)} → Tokens: {tokens} → Resultado: {intento}")
            if tokens > mejor_puntaje:
                mejor_puntaje = tokens
                mejor_descifrado = intento
                mejor_clave = clave

        # Muestra el mejor resultado encontrado
        if mejor_puntaje > 0:
            print("\n[✓] Clave más probable encontrada:", mejor_clave)
            print("[✓] Tokens reconocidos:", mejor_puntaje)
            print("Texto descifrado:\n", mejor_descifrado)
        else:
            print("\n[✗] No se encontró una clave válida que produzca texto legible.")

    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'rockyou_3000.txt'. Asegúrate de que esté en la misma carpeta.")
