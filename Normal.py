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
mensaje = ABCBRAILLE.AsignaBraille(ABCBRAILLE.AsignaASCII("""xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"""))
Hojas = math.ceil(len(mensaje)/(Dimensiones.Caracteres*Dimensiones.Renglones))

Envio=""
acumulado = 0
for h in range(Hojas):
    for n in range(Dimensiones.Renglones):
        for j in range(Dimensiones.filas):
            for l in range(Dimensiones.Caracteres):
                for m in range(Dimensiones.columnas):
                    if not (l+acumulado >= len(mensaje)):
                        print(mensaje[l+acumulado][j][m], end=' ')
                        if mensaje[l+acumulado][j][m] == 1:
                            x.append((Dimensiones.Mizq)+(Dimensiones.a*m)+(Dimensiones.c*l))
                            y.append((Dimensiones.Msup)+(Dimensiones.b*j)+(Dimensiones.d*n))
                            Envio = Envio + "G:0" + '\n'
                            Envio = Envio + (("C:" + str((Dimensiones.Mizq)+(Dimensiones.a*m)+(Dimensiones.c*l)) + 
                                "," + str((Dimensiones.Msup)+(Dimensiones.b*j)+(Dimensiones.d*n)))) + '\n'
                            Envio = Envio + "G:100" + '\n'
                    else:
                        print("Cambio")
                        print(Envio)
                        Previsualizar(x,y)
                        print(Hojas)
                        break
                print(end=' ')
            print(end='\n')
        acumulado = acumulado + l + 1
        print(end='\n')
    Envio = Envio + "H" + '\n'
Envio = Envio + "f" + '\n'

