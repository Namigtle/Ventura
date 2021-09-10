from tkinter import Frame
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import ABCBRAILLE
import math


def Previsualizar(x, y):
    plt.plot(x, y, "o", color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Previsualización')
    plt.show()
    plt.show()


class Dimensiones:
    a = 2.5
    b = 2.5
    c = 6.26
    d = 10.36
    Mizq = 30  # Margen izquierdo
    Msup = 25  # Margen superior
    Caracteres = 24  # Caracteres por renglon
    Renglones = 24  # Renglones por hoja
    filas = 3
    columnas = 2
    MatPos = [["a", "b"],
              ["c", "d"],
              ["e", "f"]]


def Traduccion(Mensaje1):
    ruta = filedialog.asksaveasfilename(title="Guardadar como:", filetypes=(
        ('text files', '*.txt'), ('All files', '*.*')))
    archivo = open(ruta, 'w', encoding="utf-8")
    Mensaje = ABCBRAILLE.AsignaBraille(ABCBRAILLE.AsignaASCII(Mensaje1))
    Hojas = math.ceil(
        len(Mensaje)/(Dimensiones.Caracteres*Dimensiones.Renglones))
    x = []
    y = []
    Envio = ""
    acumulado = 0
    finalizado = True
    h = 0
    while (h < Hojas) and finalizado:
        n = 0
        while (n < Dimensiones.Renglones) and finalizado:
            j = 0
            while (j < Dimensiones.filas) and finalizado:
                l = 0
                while (l < Dimensiones.Caracteres) and finalizado:
                    m = 0
                    while (m < Dimensiones.columnas) and finalizado:
                        if l+acumulado < len(Mensaje):
                            if Mensaje[l+acumulado][j][m] == 1:
                                x.append(216-((Dimensiones.Mizq) +
                                         (Dimensiones.a*m)+(Dimensiones.c*l)))
                                y.append(((Dimensiones.Msup) +
                                         (Dimensiones.b*j)+(Dimensiones.d*n)))
                                archivo.write("G:42"+'\n')
                                archivo.write('C:' + f'{216-((Dimensiones.Mizq)+(Dimensiones.a*m)+(Dimensiones.c*l)):0.3f}' +
                                              ',' + f'{((Dimensiones.Msup)+(Dimensiones.b*j)+(Dimensiones.d*n)):0.3f}' + '\n')
                                archivo.write("G:49"+'\n')
                        else:
                            l = Dimensiones.Caracteres
                            if j > 1:
                                finalizado = False
                        m += 1
                    l += 1
                j += 1
            acumulado = acumulado + l
            n += 1
        h += 1
        Previsualizar(x,y)
        x = []
        y = []
        if finalizado and h < Hojas:
            archivo.write("G:42"+'\n')
            archivo.write("C:" + str(Dimensiones.Mizq) +
                          "," + "300.0000" + '\n')
            archivo.write("H"+'\n')
    archivo.write("f"+'\n')
    archivo.close()


Traduccion("""hola mundo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa adios mundo""")