import math
import time
from tkinter.constants import TRUE

abecedario=[ [[0,0],
              [0,0],
              [0,0]],

             [[0,0],
              [0,0],
              [0,0]],

             [[0,0],
              [0,0],
              [0,0]],

             [[0,0],
              [0,0],
              [0,0]],

             [[0,0],
              [0,0],
              [0,0]],

             [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              [[0,0],
              [0,0],
              [0,0]],

              #signos de puntuacion

                  [[0,0],
                  [1,1],
                  [1,0]],

                  [[0,0],
                  [1,0],
                  [1,1]],

                  [[0,0],
                  [0,0],
                  [0,0]],

                  [[0,0],     
                  [0,0],
                  [0,0]],

                  [[0,0],
                  [0,0],
                  [0,0]],

                  [[1,1],
                  [1,0],
                  [1,1]],

                  [[0,0],
                  [0,0],
                  [0,0]],

                  [[1,0],
                  [1,0],
                  [0,1]],

                  [[0,1],
                  [0,1],
                  [1,0]],

                  [[0,0],
                  [0,1],
                  [1,0]],

                  [[0,0],
                  [1,1],
                  [1,0]],

                  [[0,0],
                  [1,0],
                  [0,0]],

                  [[0,0],
                  [0,0],
                  [1,1]],

                  [[0,0],
                  [0,0],
                  [1,0]],

                  [[0,0],
                  [0,0],
                  [0,0]],

        #numeros
            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],


                #signos de puntuación
                    [[0,0],
                    [1,1],
                    [0,0]],

                    [[0,0],
                    [1,0],
                    [1,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [1,1],
                    [1,1]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [1,0],
                    [0,1]],

                    [[0,0],
                    [0,1],
                    [0,0]],
        #letras mayusculas
            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            #signografia basica
                    [[1,0],
                    [1,1],
                    [1,1]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,1],
                    [1,1],
                    [1,1]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

        #letras minusculas
            [[1,0],
            [0,0],
            [0,0]],

            [[1,0],
            [1,0],
            [0,0]],

            [[1,1],
            [0,0],
            [0,0]],

            [[1,1],
            [0,1],
            [0,0]],

            [[1,0],
            [0,1],
            [0,0]],

            [[1,1],
            [1,0],
            [0,0]],

            [[1,1],
            [1,1],
            [0,0]],

            [[1,0],
            [1,1],
            [0,0]],

            [[0,1],
            [1,0],
            [0,0]],

            [[0,1],
            [1,1],
            [0,0]],

            [[1,0],
            [0,0],
            [1,0]],

            [[1,0],
            [1,0],
            [1,0]],

            [[1,1],
            [0,0],
            [1,0]],

            [[1,1],
            [0,1],
            [1,0]],

            [[1,0],
            [0,1],
            [1,0]],

            [[1,1],
            [1,0],
            [1,0]],

            [[1,1],
            [1,1],
            [1,0]],

            [[1,0],
            [1,1],
            [1,0]],

            [[0,1],
            [1,0],
            [1,0]],

            [[0,1],
            [1,1],
            [1,0]],

            [[1,0],
            [0,0],
            [1,1]],

            [[1,0],
            [1,0],
            [1,1]],

            [[0,1],
            [1,1],
            [0,1]],

            [[1,1],
            [0,0],
            [1,1]],

            [[1,1],
            [0,1],
            [1,1]],

            [[1,0],
            [0,1],
            [1,1]],

                #signografia basica doble matriz
                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

                    [[0,0],
                    [0,0],
                    [0,0]],

        #letras sin traduccion
            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[1,1],
            [1,1],
            [1,1]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],
        #vocales con acento
            [[1,0],
            [1,1],
            [1,1]],

            [[0,1],
            [0,0],
            [1,0]],

            [[0,1],
            [1,0],
            [0,1]],

            [[0,1],
            [1,1],
            [1,1]],

            [[1,1],
            [1,1],
            [0,1]],  
        #caracteres sin traduccion
            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [1,0],
            [0,1]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [1,1],
            [1,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],
        
            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],  #47

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]], #60

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[0,0],
            [0,0],
            [0,0]],

            [[1,1],
            [1,1],
            [1,1]],

            [[1,1],
            [1,1],
            [1,1]], 

            [[1,0],
            [0,0],
            [0,0]],

            [[0,1],
            [0,1],
            [1,1]]]#codigo no255      

#print(abecedario[ord("ý")])

class Margen:
    Superior = 25
    Inferior = 25
    Izquierda = 30
    Derecha = 30
class Dimensiones:
    a=2.5
    b=2.5
    c=6.26
    d=10.36

def ObtenerGrupo(letra): # Obtiene el grupo de una letra
    grupos=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0, 
            0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Arreglo de grupos 
    if grupos[ord(letra)] == 0: # si el grupo es 0
        grupo = 'letra normal'
    elif grupos[ord(letra)] == 1: # si el grupo es 1
        grupo = 'letra Mayuscula'
    elif grupos[ord(letra)] == 2: # si el grupo es 2
        grupo = 'Numero'
    return grupo # Regresa el grupo de la letra ingresada
def AsignaASCII(Mensaje):
    ArregloASCII=[] # arreglo que guardara todos los codigos ascci
    for x in range(len(Mensaje)): # x incrementa de 0 hasta el tamaño del mensaje
        if ObtenerGrupo(Mensaje[x]) == 'letra normal': # Si es letra normal
            ArregloASCII.append(ord(Mensaje[x])) # Agrega el codigo ASCII de la letra al arreglo
        elif ObtenerGrupo(Mensaje[x]) == 'letra Mayuscula': # Si es letra Mayuscula
            ArregloASCII.append(254) # Agrega el codigo ASCII del simbolo al arreglo
            ArregloASCII.append(ord(Mensaje[x])) # Agrega el codigo ASCII de la letra al arreglo
        elif ObtenerGrupo(Mensaje[x]) == 'Numero': # Si es numero
            ArregloASCII.append(255) # Agrega el codigo ASCII del simbolo
            ArregloASCII.append(ord(Mensaje[x])) # Agrega el codigo ASCII de la ldetra al arreglo
    return ArregloASCII # Regresa el arreglo con todos los codigos ASCII de las letras y simbolos correspondientes
def AsignaBraille(ArregloAscii):
    TextoBraille=[] # variable para el texto traducido al braille 
    Entradas=[] # variable de salida con las columnas de cada letra
    for x in range(len(ArregloAscii)): # recorre todo el arreglo Ascii
        TextoBraille.append(abecedario[ArregloAscii[x]]) # agrega las 
                        # letras braille dependiendo de su codigo ASCII
    for z in range(len(TextoBraille)): # recorre todo el texto traducido
        for y in range(len(TextoBraille[z][0])): # recorre cada columna
            Entradas.append([TextoBraille[z][2][y],
            TextoBraille[z][1][y],TextoBraille[z][0][y]]) # agrega columna 
            # por columna de cada letra braille a la variable de salida
    return TextoBraille # regresa el arreglo de salida 
def ObtenerCoordenadas(CantidadCaracteres):
    Ancho = 210 # ancho de la hoja
    Largo = 297 # largo de la hoja
    EnviaXY=[] # arreglo de coordenadas X y Y
    Ncaracteres = round((Ancho-(Margen.Izquierda+Margen.Derecha))/
    (Dimensiones.c)) # Calcula el numero de caracteres que tendra la hoja por cada renglon
    Nrenglones = round((Largo-(Margen.Superior+Margen.Inferior))/
    (Dimensiones.d)) # Calcula el numero de renglones que tendra la hoja
    Nhojas = math.ceil(CantidadCaracteres/(Ncaracteres*
    Nrenglones))
    print("Hojas: ", Nhojas, "Renglones: ", Nrenglones, "Caracteres: ", Ncaracteres, end='\n')
    for item in range(Nhojas):
        for n in range(Nrenglones): # incrementa n hasta la cantidad de renglones
            for l in range(Ncaracteres): # incrementa l hasta la cantidad de caracteres
                for m in range(2): # incrementa m hasta 2
                    Cx = (Margen.Izquierda)+(Dimensiones.a*
                    m)+(Dimensiones.c*l) # Calcula la coordenada X de cada punto  
                    Cy = (Margen.Superior+
                    Dimensiones.b)+(Dimensiones.d*n) # Calcula la coordenada Y de cada punto
                    EnviaXY.append([Cx, Cy]) # Agrega las coordenadas X y Y al arreglo EnviaXY
    EnviaXY.append([Cx,Cy])
    return EnviaXY # Regresa el arreglo como parametro de salida de la función 

