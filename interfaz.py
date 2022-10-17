import tkinter as tk
from tkinter import ttk, DISABLED
from tkinter import messagebox



def show_frame(frame):
    frame.tkraise()
#Interfaz Grafica Configuracion
window = tk.Tk()
window.geometry("500x500")
window.title("Museo AstronomoTEC")
colorVentana = "#CADBC8"
colorBoton = "#9C9583"
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#Declaracion de frames o pantallas
menuPrincipal = tk.Frame(window, bg=colorVentana)
frame2 = tk.Frame(window, bg=colorVentana)

for frame in (menuPrincipal,frame2):
    frame.grid(row=0, column=0, sticky="nsew")

#menuPrincipal
botonImportarAstronomos= tk.Button(menuPrincipal, text = "Importar Astronomos", bg=colorBoton, command=lambda:prueba())
botonImportarAstronomos.place(relx=0.5,
                            rely=0.1,
                            anchor='center')
botonCrearVisitante= tk.Button(menuPrincipal, text = "Crear un Visitante", bg=colorBoton, state=DISABLED)
botonCrearVisitante.place(relx=0.5,
                            rely=0.2,
                            anchor='center')
botonCrearBDVisitante= tk.Button(menuPrincipal, text = "Crear BD de Visitante", bg=colorBoton, state=DISABLED)
botonCrearBDVisitante.place(relx=0.5,
                            rely=0.3,
                            anchor='center')
botonAsignarFans= tk.Button(menuPrincipal, text = "Asignar Astronomos Fans", bg=colorBoton, state=DISABLED)
botonAsignarFans.place(relx=0.5,
                            rely=0.4,
                            anchor='center')
botonCargarBiblioteca= tk.Button(menuPrincipal, text = "Cargar Biblioteca Digital", bg=colorBoton, state=DISABLED)
botonCargarBiblioteca.place(relx=0.5,
                            rely=0.5,
                            anchor='center')
botonDarDeBaja= tk.Button(menuPrincipal, text = "Dar de Baja", bg=colorBoton, state=DISABLED)
botonDarDeBaja.place(relx=0.5,
                            rely=0.6,
                            anchor='center')
botonReportes= tk.Button(menuPrincipal, text = "Reportes", bg=colorBoton, state=DISABLED)
botonReportes.place(relx=0.5,
                            rely=0.7,
                            anchor='center')
botonSalir= tk.Button(menuPrincipal, text = "Salir", bg=colorBoton,)
botonSalir.place(relx=0.5,
                            rely=0.8,
                            anchor='center')
def prueba():
    botonCrearVisitante["state"] ="normal"
    botonCrearBDVisitante["state"] = "normal"
    botonDarDeBaja["state"] = "normal"

show_frame(menuPrincipal)
window.mainloop()