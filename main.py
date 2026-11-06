# Clase 14 mayo 2026
# Aplicación con varias pantallas y botones para navegar entre ellas
# usaremos un archivo .kv para definir la interfaz gráfica

import os  # CAMBIO 1 (ver README): para averiguar en qué carpeta está este archivo

from kivy.lang import Builder
from kivy.app import App
from kivy.resources import resource_add_path  # CAMBIO 1
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

# CAMBIO 1: carpeta donde vive este archivo. En el PC es la carpeta del proyecto; en el
# teléfono es la carpeta privada donde Android/iOS instala la app. Así el código no depende
# de "desde qué carpeta se ejecutó".
BASE = os.path.dirname(os.path.abspath(__file__))
# Le decimos a Kivy que busque ahí también las imágenes (App_dino1.jpg, etc.) que se
# nombran dentro del archivo .kv.
resource_add_path(BASE)

class Pantalla1(Screen):
    pass

class Pantalla2(Screen):
    pass

class Pantalla3(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# CAMBIO 2: antes era Builder.load_file("App_juego.kv"), una ruta relativa que solo funciona
# si el programa se lanza desde la misma carpeta. Ahora la ruta es absoluta (BASE + nombre).
kv = Builder.load_file(os.path.join(BASE, "App_juego.kv"))

class AppJuego(App):
    #Window.clearcolor = (.5, 1, .2, 1)  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana
    
    def build(self):
        return kv

if __name__ == "__main__":
    AppJuego().run()