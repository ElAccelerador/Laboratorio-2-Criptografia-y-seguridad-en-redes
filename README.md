# PythonAttack: Ataque de Fuerza Bruta en DVWA

Este repositorio contiene un script en Python diseñado para realizar un ataque de fuerza bruta sobre el formulario de login de DVWA (Damn Vulnerable Web Application), una aplicación web diseñada para enseñar y practicar ataques de seguridad.

## 📂 Archivos principales

- `PythonAttack.py`: Script en Python para realizar un ataque de fuerza bruta sobre el formulario de login de DVWA, utilizando combinaciones de usuarios y contraseñas desde archivos de texto. Para que todo funcione correctamente deben estar en el mismo directorio.
  
## ⚙️ Requisitos

- Python 3.x
- [requests](https://pypi.org/project/requests/): `pip install requests`

## 🚀 Cómo usar

1. **Configurar los archivos de entrada**  
   Crea los archivos `names.txt` y `passwords.txt` con las listas de nombres de usuario y contraseñas que se intentarán. Se dejarán los utilizados en el laboratorio igualmente.
   
2. **Modificar el script**
   El script utilizado deberá ser modificado, tanto el nivel de seguridad en el que se utiliza, como el valor de PHPSESSID de la Cookie utilizada.
   
3. **Ejecutar el script**  
   Ejecuta `PythonAttack.py` con el siguiente comando:
   ```bash
   python3 PythonAttack.py

4. **Verificar los resultados**
   El script intentará hacer login con todas las combinaciones de usuario y contraseña y mostrará si el login fue exitoso o no para cada combinación.

## 📸 Ejemplo de salida

```bash
Intentando: Usuario=admin | Contraseña=password
Login exitoso! Usuario: admin, Contraseña: password

Intentando: Usuario=pablo | Contraseña=123456
Login fallido para: pablo, 123456
...
