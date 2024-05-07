import random
import serial
import winsound

# Inicializar la comunicación serial con el microcontrolador
ser = serial.Serial('COM3', 9600, timeout=1)

# Función para detectar anotaciones
def detectar_anotacion(index):
    if index == "AN 1":
        # Seleccionar aleatoriamente uno de tres grupos de 2 paletas contiguas
        paletas = [1, 2, 3, 4, 5, 6]
        random.shuffle(paletas)
        paletas_seleccionadas = paletas[:2]
        if any(paleta in paletas_seleccionadas for paleta in paletas):
            return False
        else:
            return True
    elif index == "AN 2":
        # Seleccionar aleatoriamente 3 paletas contiguas
        paletas = [1, 2, 3, 4, 5, 6]
        random.shuffle(paletas)
        paletas_seleccionadas = paletas[:3]
        if any(paleta in paletas_seleccionadas for paleta in paletas):
            return False
        else:
            return True
    elif index == "AN 3":
        # Seleccionar aleatoriamente uno de dos conjuntos de tres paletas alternas
        paletas = [1, 2, 3, 4, 5, 6]
        random.shuffle(paletas)
        paletas_seleccionadas = paletas[:3]
        if any(paleta in paletas_seleccionadas for paleta in paletas):
            return False
        else:
            return True
    else:
        return None

# Función para encender LEDs
def encender_led(index):
    if index == "local":
        ser.write(b'H')
    elif index == "visitante":
        ser.write(b'I')

# Función para generar sonidos de porras
def generar_porras():
    # Generar un número aleatorio entre 1 y 3
    porra = random.randint(1, 3)
    if porra == 1:
        # Sonido de celebración de gol
        winsound.Beep(2500, 1000)
    elif porra == 2:
        # Sonido de celebración de gol
        winsound.Beep(2000, 1000)
    else:
        # Sonido de celebración de gol
        winsound.Beep(1500, 1000)

# Función para generar sonidos de abucheos
def generar_abucheos():
    # Generar un número aleatorio entre 1 y 3
    abucheos = random.randint(1, 3)
    if abucheos == 1:
        # Sonido de abucheos
        winsound.Beep(1000, 500)
    elif abucheos == 2:
        # Sonido de abucheos
        winsound.Beep(1200, 500)
    else:
        # Sonido de abucheos
        winsound.Beep(1300, 500)

# Función para detectar gol
def detectar_gol():
    # Leer el estado de las paletas
    paletas_estado = ser.read(6)
    # Verificar si se ha golpeado una paleta
    if paletas_estado[0] == b'1':
        # Generar sonido de porras
        generar_porras()
        # Encender el LED del equipo en turno
        encender_led("local")
    elif paletas_estado[1] == b'1':
        # Generar sonido de abucheos
        generar_abucheos()
        # Encender el LED del equipo en turno
        encender_led("visitante")

# Iniciar el juego
while True:
    # Seleccionar un índice de la posición del portero
    index = random.choice(["AN 1", "AN 2", "AN 3"])
    # Detectar anotaciones
    if detectar_anotacion(index):
        # Detectar gol
        detectar_gol()
    else:
        # No se ha anotado
        pass