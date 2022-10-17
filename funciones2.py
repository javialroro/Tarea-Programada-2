import tkinter as tk
import random
import names




ventana = tk.Tk()



def seleccionMatriz():
    if seleccion.get() == 1:
        lblmensaje1 = tk.Label(ventana,text = 'Digite la cantidad de visitantes que desea. Min 0. Max 1000.').pack()
        seleccion2 = tk.Entry(ventana)
        seleccion2.pack()
        boton1 = tk.Button(ventana, text = 'Escoger cantidad. ', command = lambda: crearMatriz(seleccion2.get()))
        boton1.pack()

def generadorID():
    num = ''
    for i in range(9):
        if i == 0:
            num += str(random.randint(1,9))
        elif i != 1 and i != 5:
            num += str(random.randint(0,9))
        else:
            num += '0'
    return num 

def crearMatriz(cantidad):
    cantidad = int(cantidad)
    visitantes = []
    for i in range(cantidad):
        visitante = []
        visitante.append(generadorID())
        visitante.append(tuple((names.get_full_name()+" "+names.get_last_name()).split()))
        visitante.append([])
        visitante.append([])
        visitante.append(True)
        visitantes.append(visitante)
        textoVisitantes = ''' '''
    print(visitantes)
        
seleccion = tk.IntVar()


rbnCrear = tk.Radiobutton(ventana, text = 'Crear', variable = seleccion, value = 1, command = seleccionMatriz).pack(anchor = tk.W) 

rbnLimpiar = tk.Radiobutton(ventana, text = 'Limpiar', variable = seleccion, value = 2, command = seleccionMatriz).pack(anchor = tk.W)




ventana.mainloop()







def Matriz(cantidad):
    visitantes = []
    for i in range(cantidad):
        visitante = []
        visitante.append(generadorID())
        visitante.append(tuple((names.get_full_name()+" "+names.get_last_name()).split()))
        visitante.append([])
        visitante.append([])
        visitante.append(True)
        visitantes.append(visitante)
    return visitantes
