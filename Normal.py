import matplotlib.pyplot as plt
import numpy as np
import ABCBRAILLE
import math
def Previsualizar(x,y):
    plt.plot(x,y,"o", color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Previsualización')
    plt.show()
    plt.show()
class Dimensiones:
    a=2.5
    b=2.5
    c=6.26
    d=10.36
    Mizq=30 # Margen izquierdo
    Msup=25 # Margen superior
    Caracteres=24 # Caracteres por renglon
    Renglones=24 # Renglones por hoja
    filas=3 
    columnas=2
    MatPos= [   ["a","b"],
                ["c","d"],
                ["e","f"]]
x=[]
y=[]
mensaje = ABCBRAILLE.AsignaBraille(ABCBRAILLE.AsignaASCII("""
hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo
hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo hola mundo"""))
Hojas = math.ceil(len(mensaje)/(Dimensiones.Caracteres*Dimensiones.Renglones))

Envio = ""
acumulado = 0
finalizado = True
h=0
while (h<Hojas) and finalizado:
    n=0
    while (n<Dimensiones.Renglones) and finalizado:
        j=0
        while (j<Dimensiones.filas) and finalizado:
            l=0
            while (l<Dimensiones.Caracteres) and finalizado:
                m=0
                while (m<Dimensiones.columnas) and finalizado:
                    if l+acumulado < len(mensaje):
                        #print(mensaje[l+acumulado][j][m], end=' ')
                        if mensaje[l+acumulado][j][m] == 1:
                            x.append((Dimensiones.Mizq)+(Dimensiones.a*m)+(Dimensiones.c*l))
                            y.append((Dimensiones.Msup)+(Dimensiones.b*j)+(Dimensiones.d*n))
                            Envio = Envio + "G:0" + '\n'
                            Envio = Envio + (("C:" + str((Dimensiones.Mizq)+(Dimensiones.a*m)+(Dimensiones.c*l)) + 
                                "," + str((Dimensiones.Msup)+(Dimensiones.b*j)+(Dimensiones.d*n)))) + '\n'
                            Envio = Envio + "G:100" + '\n'
                    else:
                        l=Dimensiones.Caracteres
                        if j>1:
                            finalizado = False
                    m+=1
                #print(end=' ')
                l+=1
            #print(end='\n')
            j+=1
        acumulado += 1
        #print(end='\n')
        n+=1
    if finalizado:
        Envio = Envio + "H" + '\n'
        Previsualizar(x,y)
        x=[]
        y=[]
    h+=1
Envio = Envio + "f" + '\n'

print("Cambio")
#print(Envio)

print(Hojas)
