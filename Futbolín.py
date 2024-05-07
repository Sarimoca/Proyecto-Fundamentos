from tkinter import *
from PIL import Image, ImageTk
import pygame

pygame.init()
pygame.mixer.music.load("Musica y sonidos/Menu.mp3")
pygame.mixer.music.play(-1)

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2) - (600 / 2)

    window.geometry('%dx%d+%d+%d' % (800, 600, x, y))
    window.resizable(False, False)

def acerca_de():
    global window, bg_imagen_pi_1
    window = canva_info = Toplevel()
    canva_info.title("Acerca de")
    canva_info.geometry("800x600")
    canva_info.resizable(False, False)

    imagen_info = PhotoImage(file="Imagenes/pantalla-de-informacion-complementaria.gif")
    bg_imagen_pi_1 = imagen_info.subsample(3, 3)
    bg_imagen_pi = Label(canva_info, image=bg_imagen_pi_1, bg="black")
    bg_imagen_pi.place(x=0, y=0, relheight=1, relwidth=1)
    center_window(window)

def configuracion_inicial():
    ventana = Toplevel()
    ventana.title("Configuración inicial")
    Label(ventana, text="Configuración inicial del juego...").pack()
    ventana.geometry("800x600")
    center_window(ventana)
    ventana.configure(bg="black")
    
    equipo_var = StringVar()
    jugador_var = StringVar()

    # Suponiendo una estructura de datos para los equipos y jugadores
    equipos = {
        "equipo1": {"nombre": "Equipo 1", "jugadores": ["Jugador1", "Jugador2", "Jugador3", "Portero1", "Portero2", "Portero3"]},
        "equipo2": {"nombre": "Equipo 2", "jugadores": ["Jugador1", "Jugador2", "Jugador3", "Portero1", "Portero2", "Portero3"]},
        "equipo3": {"nombre": "Equipo 3", "jugadores": ["Jugador1", "Jugador2", "Jugador3", "Portero1", "Portero2", "Portero3"]}
    }

    def select_equipo(equipo):
        equipo1_button.config(bg='SystemButtonFace')
        equipo2_button.config(bg='SystemButtonFace')
        equipo3_button.config(bg='SystemButtonFace')
        
        if equipo == "equipo1":
            equipo1_button.config(bg='gray')
        elif equipo == "equipo2":
            equipo2_button.config(bg='gray')
        elif equipo == "equipo3":
            equipo3_button.config(bg='gray')

        equipo_var.set(equipo)

    def mostrar_seleccion_jugadores():
        equipo = equipo_var.get()
        if not equipo:
            return  # No hay equipo seleccionado
        
        ventana_jugadores = Toplevel(ventana)
        ventana_jugadores.title("Selecciona los jugadores")
        ventana_jugadores.geometry("400x300")
        ventana_jugadores.configure(bg="black")
        
        Label(ventana_jugadores, text="Selecciona un jugador", bg="black", fg="white").pack()

        jugadores_frame = Frame(ventana_jugadores, bg="black")
        jugadores_frame.pack(expand=True, fill=BOTH)

        # Imágenes de los botones de jugadores
        balon_image = ImageTk.PhotoImage(Image.open("Imagenes/Balon.png").resize((50, 75)))

        for jugador in equipos[equipo]["jugadores"]:
            jugador_button = Button(jugadores_frame, image=balon_image, bg='SystemButtonFace',
                                    command=lambda j=jugador: jugador_var.set(j))
            jugador_button.image = balon_image  # keep a reference!
            jugador_button.pack(pady=10)

    equipo_frame = Frame(ventana, bg="black")
    equipo_frame.pack(expand=True, fill=BOTH)

    equipo1_image = ImageTk.PhotoImage(Image.open("Imagenes/Balon.png").resize((100, 150)))
    equipo1_button = Button(equipo_frame, image=equipo1_image, command=lambda: select_equipo("equipo1"))
    equipo1_button.grid(row=1, column=0, padx=10, pady=10)

    equipo2_image = ImageTk.PhotoImage(Image.open("Imagenes/Balon.png").resize((100, 150)))
    equipo2_button = Button(equipo_frame, image=equipo2_image, command=lambda: select_equipo("equipo2"))
    equipo2_button.grid(row=1, column=1, padx=10, pady=10)

    equipo3_image = ImageTk.PhotoImage(Image.open("Imagenes/Balon.png").resize((100, 150)))
    equipo3_button = Button(equipo_frame, image=equipo3_image, command=lambda: select_equipo("equipo3"))
    equipo3_button.grid(row=1, column=2, padx=10, pady=10)

    Label(equipo_frame, text="Equipo 1", bg="black", fg="white").grid(row=0, column=0)
    Label(equipo_frame, text="Equipo 2", bg="black", fg="white").grid(row=0, column=1)
    Label(equipo_frame, text="Equipo 3", bg="black", fg="white").grid(row=0, column=2)

    # Botón para ir a la selección de jugadores después de elegir el equipo
    Button(ventana, text="Jugar", command=mostrar_seleccion_jugadores, bg="grey", fg="white").pack(pady=20)

configuracion_inicial()
        
def preliminares_juego():
    ventana = Toplevel()
    ventana.title("Preliminares de juego")
    Label(ventana, text="Preliminares de juego...").pack()
    ventana.geometry("800x600")
    center_window(ventana)
    ventana.configure(bg="black")

ventana_principal = Tk()
ventana_principal.title("Menú principal")
ventana_principal.geometry("800x600")
center_window(ventana_principal)
ventana_principal.configure(bg="black")

boton_acerca_de = Button(ventana_principal, text="Acerca de", command=acerca_de, height=2, width=20)
boton_acerca_de.grid(row=3, column=0)
boton_acerca_de.place(relx=0.5, rely=0.7, anchor=CENTER)

boton_configuracion_inicial = Button(ventana_principal, text="Configuración inicial", command=configuracion_inicial, height=2, width=20)
boton_configuracion_inicial.grid(row=2, column=0)
boton_configuracion_inicial.place(relx=0.5, rely=0.6, anchor=CENTER)

boton_preliminares_juego = Button(ventana_principal, text="Preeliminares del juego", command=preliminares_juego, height=2, width=20)
boton_preliminares_juego.grid(row=1, column=0)
boton_preliminares_juego.place(relx=0.5, rely=0.5, anchor=CENTER)

ventana_principal.mainloop()