# Este script adicional foi construído para captar a localização do ponteiro em locais específicos da tela

# Basta executá-lo e posicionar o ponteiro aonde se quer captar a localização. A captação se da em um período de tempo pré-estabelecido.

import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(200)