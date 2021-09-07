import matplotlib.pyplot as plt
import numpy as np

def Previsualizacion(Coordenadas):
    x=[]
    y=[]
    for item in range(len(Coordenadas)):
        x.append(Coordenadas[item][0])
        y.append(Coordenadas[item][1])
    plt.plot(x,y,"o", color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Previsualización')
    plt.show()

