import tkinter as tk

#crear ventana 
ventana = tk.Tk()
ventana.geometry('300x300') #tamanno

def saludo(nombre): #funcion ejemplo
    print('hola ' + nombre)   

cajaTexto = tk.Entry(ventana)
cajaTexto.pack()

etiquetaCajaTexto = tk.Label(ventana)
etiquetaCajaTexto.pack()


def sacarTexto(): # funcion para imprimir el texto de la caja, en la consola.
    imprimir = cajaTexto.get()
    print(imprimir)

def imprimirEtiqueta():
    impresion = cajaTexto.get()
    etiquetaCajaTexto['text'] = impresion

boton = tk.Button(ventana, text = 'ingrese: ', command = imprimirEtiqueta)
boton.pack()
#boton.grid(row = 0, column = 2) #posicion del boton(widget) en una matriz de 4x4
# etiqueta = tkinter.Label(ventana, text =  'Ingrese cantidad que desea en matriz') #texto en la ventana, se le puede poner color en el fondo con
# etiqueta.pack() #funcion que automaticamente acomoda la etiqueta, se puede personalizar el lugar de esta  #                        ,bg = 'blue

# boton1 = tkinter.Button(ventana,text = 'presiona', command = lambda: saludo('python')) # agregar boton, lambda es para imprimir algo cuando sale se presiona boton
# boton1.pack()                                                                          # ya sea string o con alguna funcion

ventana.mainloop()

