[app]

# --- Identidad de la app ---------------------------------------------------------------
# Nombre que se ve bajo el icono en el teléfono.
title = Juego Dinos
# Nombre interno del paquete. Solo minúsculas y números, SIN espacios ni guiones bajos.
package.name = juegodinos
# "Dominio al revés" que, junto a package.name, forma el identificador único de la app:
# org.clase.juegodinos. Android no deja instalar dos apps con el mismo identificador.
package.domain = org.clase
version = 0.1

# --- Qué archivos entran al APK --------------------------------------------------------
# Carpeta con el código (el punto = la raíz del repositorio). Ahí debe estar main.py.
source.dir = .
# Solo se empaquetan archivos con estas extensiones. OJO: si falta "jpg" aquí, las imágenes
# NO entran al APK y la app muestra los fondos vacíos SIN dar ningún error.
source.include_exts = py,png,jpg,kv,atlas
# Carpetas que NO deben entrar (las capturas de docs/ son .png y entrarían por error).
source.exclude_dirs = docs,.github,.git

# --- Qué necesita la app para funcionar ------------------------------------------------
# Lista de paquetes de Python que la app usa. python3 + kivy bastan: este juego solo usa Kivy.
# (Si algún día usas otra librería, se añade aquí, separada por comas.)
requirements = python3,kivy

# --- Pantalla --------------------------------------------------------------------------
# La ventana original es de 600x400 (apaisada), así que la app se fija en horizontal.
orientation = landscape
fullscreen = 0

# --- Versión de Android ----------------------------------------------------------------
# Arquitecturas de CPU para las que se compila: arm64-v8a = casi todos los teléfonos
# actuales; x86_64 = emuladores de Android en PC.
android.archs = arm64-v8a, x86_64
# API 33 = Android 13. Es la combinación probada con la versión de python-for-android de abajo.
android.api = 33
android.ndk = 25b
# Google obliga a aceptar la licencia del Android SDK antes de descargarlo. Normalmente el
# programa pregunta "Accept? (y/N)"; en GitHub Actions no hay nadie para contestar, y sin esta
# línea el SDK NO se instala y el build falla con "Aidl not found" / "license not accepted".
android.accept_sdk_license = True

# --- python-for-android (p4a) ------------------------------------------------------------
# Es el programa que realmente empaqueta Python y Kivy dentro del APK. Se FIJA a una versión
# concreta (etiqueta v2024.01.21): la última ("master") usa Python 3.14, con el que Kivy 2.3
# no compila. Fijar la versión hace que el resultado sea siempre el mismo.
p4a.branch = v2024.01.21

[buildozer]
# 2 = mostrar todos los detalles en el log (útil para encontrar errores).
log_level = 2
# Avisa si se ejecuta como root. En GitHub Actions se ejecuta como root; es solo un aviso.
warn_on_root = 1
