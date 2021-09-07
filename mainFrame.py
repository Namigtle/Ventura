from tkinter import Frame
from tkinter import *
from tkinter import filedialog
import time
import tkinter as tk
import tkinter.scrolledtext as st
from typing import TextIO
from matplotlib.pyplot import colorbar
import serial.tools.list_ports
import ABCBRAILLE
import LevaBraille
import serial
import Grafica
import math

comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=900, height=800)
        self.master=master
        self.pack(side="left")
    # Variables del Panel conexión:
        self.SerialArduino=serial
        self.VarPuerto=StringVar() # Valor seleccionado del menú: puertos COM
        self.VarVelocidades=StringVar() # Valor seleccionado del menú: velocidades
        self.MenuVelocidades=['4800','9600','19200', # Velocidades disponobles
        '38400','57600','115200','460800']
        self.MenuPuertosCom=connected # Puertos disponibles
        self.PanelConexion=tk.PhotoImage(file="PanelCom.png") # imagen del panel
        self.BotonConectar=tk.PhotoImage(file="Conectar.png") # imagen del botón 
        self.BotonDesconectar=tk.PhotoImage(file="Desconectar.png") # imagen del botón 
        self.BotonActualizar=tk.PhotoImage(file="BotAct.png") # imagen del botón
        self.BotonGuardar=tk.PhotoImage(file="BotGua.png") # imagen del botón
    # Variables del Panel manipular maquina:
        self.PanelManipularMaquina=tk.PhotoImage( # imagen del panel
        file="PanelControlXY.png")
        self.MenuResoluciones=['10','20', # Resoluciones disponibles
        '30','40','50','100','1000']
        self.VarResolucion = StringVar() # Valor seleccionado del menú: resolución 
        self.BotonFlechaDerecha = tk.PhotoImage(file= # imagen del botón 
        "FlechaDer.png")
        self.BotonFlechaIzquierda = tk.PhotoImage(file= # imagen del botón 
        "FlechaIz.png")
        self.BotonFlechaArriba = tk.PhotoImage(file= # imagen del botón 
        "FlechaArr.png")
        self.BotonFlechaAbajo = tk.PhotoImage(file= # imagen del botón 
        "FlechaAb.png")
        self.BotonGrabar = tk.PhotoImage(file="BotGra.png")
    # Variables del Panel abrir archivo: 
        self.Dispositivo = serial.Serial() # Objeto Arduino
        self.PanelArchivo=tk.PhotoImage(file="PanelImp.png") # Imagen del panel
        self.CapturaTexto = StringVar() # Variable a la que se le asigna 
                                        # el texto ingresado manualmente 
        self.LecturaArchivo=StringVar() # Variable a la que se le asigna el texto 
                                        # ingresado a travez de un archivo
        self.EnviarParametros=StringVar() # Variable a la que se le asigna el texto traducido 
        self.BotonAbrir = tk.PhotoImage(file="Abrir.png") # imagen del botón 
        self.BotonTraducir = tk.PhotoImage(file="ImTraducir.png") # imagen del botón 
        self.BotonImprimir = tk.PhotoImage(file="ImImprimir.png") # imagen del botón
        self.BotonPrevisualizar = tk.PhotoImage(file="Prev.png") # imagen del botón
        self.BotonEstado = tk.PhotoImage(file="BotEst.png") # imagen del boton 
        self.create_widgets()

# Funciones del Panel conexión: 
    def ConectarArduino(self):
        try:
            self.Dispositivo = serial.Serial(format(self.VarPuerto.get()),
            int(format(self.VarVelocidades.get())),timeout=0.01) # Conecta con dispositivo
                            # tomando en cuenta el puerto, velocidad y tiempo de espera
            time.sleep(1)
            self.text_area.delete("1.0", tk.END) # limpia la terminal
            self.text_area.insert(tk.INSERT, 
            "Conexion completada exitosamente") # imprime estado en la terminal
        except:
            self.text_area.delete("1.0", tk.END) # limpia la terminal
            self.text_area.insert(tk.INSERT,
            "No se pudo conectar al dispositivo") # imprime estado en la terminal
    def ActualizarPuerto(self):
        try:
            print("Actualizado")
        except:
            pass
    def DesconectarArduino(self):
        self.Dispositivo.close()
        time.sleep(1)
        self.text_area.delete("1.0", tk.END) # limpia la terminal 
        self.text_area.insert(tk.INSERT,
        "Conexión finalizada exitosamente") # imprime estado en la terminal
# Funciones del Panel manipular maquina:
    def CarroPositivo(self):
        Mega=self.Dispositivo # Asigna el objeto serial
        Xmas = "X:"+format(self.VarResolucion.get()) # Asigna el parametro a enviar
        self.text_area.delete("1.0", tk.END) # limpia la terminal
        self.text_area.insert(tk.INSERT,Xmas+'\n') # Imprime en la terminal el parametro a enviar
        Mega.write(Xmas.encode('ascii')) # Envia el parametro al dispositivo
    def CarroNegativo(self):
        Mega=self.Dispositivo # Asigna el objeto serial
        Xmenos = "X:-"+format(self.VarResolucion.get()) # Asigna el parametro a enviar
        self.text_area.delete("1.0", tk.END) # Limpia la terminal
        self.text_area.insert(tk.INSERT,Xmenos+'\n') # Imprime en la terminla el parametro a enviar
        Mega.write(Xmenos.encode('ascii')) # Envia el parametro
    def RodilloPositivo(self):
        Mega=self.Dispositivo # Asigna el objeto serial
        Ymas = "Y:"+format(self.VarResolucion.get()) # Asigna el parametro a enviar
        self.text_area.delete("1.0", tk.END) # Limpia la terminal
        self.text_area.insert(tk.INSERT,Ymas+'\n') # Imprime el parametro
        Mega.write(Ymas.encode('ascii')) # Envia el parametro
    def RodilloNegativo(self):
        Mega=self.Dispositivo # Asigna el objeto serial
        Ymenos = "Y:-"+format(self.VarResolucion.get()) # Asigna el parametro a enviar
        self.text_area.delete("1.0", tk.END) # Limpia la terminal
        self.text_area.insert(tk.INSERT,Ymenos+'\n') # Imprime el parametro
        Mega.write(Ymenos.encode('ascii')) # Envia el parametro
    def Grabar(self):
        Mega=self.Dispositivo # Asigna el objeto serial
        Ymenos = "A" # Asigna el parametro a enviar
        Mega.write(Ymenos.encode('ascii')) # Envia el parametro
# Funciones del Panel archivo:
    def TraducirArchivo(self):
        ruta=filedialog.askopenfilename(title="Abrir") # Pregunta por la ruta y el nombre 
                                                       # del archivo al que se desea leer
        archivo = open(ruta,'r', encoding="utf-8") # Abre el archivo para su lectura
        self.LecturaArchivo=archivo.read() # Lee el contenido del archivo 
        TextoTraducido=ABCBRAILLE.AsignaBraille(ABCBRAILLE.AsignaASCII(self.LecturaArchivo)) # Traduce el contenido del archivo a braille
        Coordenadas = ABCBRAILLE.ObtenerCoordenadas(len(
            TextoTraducido)) # Extrae las coordenadas de las letras braill
        print("Tam TextoTrad: ", len(TextoTraducido), "Tam Coordenadas: ", len(Coordenadas), end='\n')
        self.EnviarParametros=LevaBraille.EnviarDatos(TextoTraducido,Coordenadas)
        self.EnviarParametros.append("f")
    def LeerCampo2(self):
        TextCampo = (self.CapturaTexto.get() + '\n')
        TextoTraducido = ABCBRAILLE.AsignaBraille(ABCBRAILLE.AsignaASCII(TextCampo))
        Coordenadas = ABCBRAILLE.ObtenerCoordenadas(len(TextoTraducido)/2)
        self.EnviarParametros=LevaBraille.EnviarDatos(TextoTraducido,Coordenadas)
        self.EnviarParametros.append("f")
    def Guardar(self):
        ruta=filedialog.asksaveasfilename(title="Guardadar como:", filetypes = (('text files', '*.txt'),('All files', '*.*')))
        archivo = open(ruta,'w',encoding="utf-8")
        for item in range(len(self.EnviarParametros)):
            archivo.write(self.EnviarParametros[item]+'\n')
        archivo.close()   
    def Imprimir(self):
        Mega=self.Dispositivo
        Mensaje=""
        for item in range(len(self.EnviarParametros)):
            Mensaje = Mensaje + self.EnviarParametros[item] + '\n'
        self.text_area.delete("1.0", tk.END)
        Mega.write("I".encode('ascii'))
        Mega.flush()
        Ciclo=False
        while not Ciclo:
            Ciclo =(Mega.readline().decode('ascii'))=='F' 
        Mega.write(Mensaje.encode('ascii'))
        Mega.flush()
        Ciclo=False
        while not Ciclo:
            Ciclo =(Mega.readline().decode('ascii'))=='F' 
        Mega.write("W".encode('ascii'))
        Mega.flush()
        Ciclo=False
        while not Ciclo:
            Ciclo =(Mega.readline().decode('ascii'))=='F' 
        Mega.close()
        self.text_area.insert(tk.INSERT,Mensaje)
    def LeerCampo(self, event):
        self.LeerCampo2()
    def Previsualizar(self):
        datos=LevaBraille.ObtenerXY(self.EnviarParametros)
        Grafica.Previsualizacion(datos)
    def Revisar(self):
        Mega = self.Dispositivo
        self.text_area.delete("1.0", tk.END)
        Mega.write("B".encode('ascii'))
        Ciclo=False
        Lectura = ""
        while not Ciclo:
            Lectura = Mega.readline().decode('ascii')
            if len(Lectura) > 1:
                if (Lectura[0] == "L"):
                    self.text_area.insert(tk.INSERT,Lectura+'\n')
                    Lectura="F"
            Ciclo =Lectura=='F'
    def create_widgets(self):

# Espacio para Panel "Manipular maquina":

        XPMM=0 # posicion del panel en X
        YPMM=100 # posicion del panel en Y
    # Etiquetas: 
        Label(self,image=self.PanelManipularMaquina, # Panel y etiquetas
        bg=("#%02x%02x%02x"%(70,70,71))).place(x=18+XPMM, y=330+YPMM)    
    # Menú de opciones:
        self.VarResolucion.set('1') # Menú de resoluciones
        OptionMenu(self,self.VarResolucion,
        *self.MenuResoluciones).place(x=152+XPMM,y=572+YPMM)
    # botones
        Button(self, image=self.BotonFlechaDerecha, 
        border="0", command=self.CarroPositivo,background
        =("#%02x%02x%02x" % (20,20,21))).place(
        x=465-300+XPMM, y =455+YPMM) # Boton flecha derecha
        Button(self, image=self.BotonFlechaIzquierda, 
        border="0", command=self.CarroNegativo,background
        =("#%02x%02x%02x" % (20,20,21))).place(
        x=365-300+XPMM, y =455+YPMM) # Boton flecha izquierda
        Button(self, image=self.BotonFlechaArriba, 
        border="0", command=self.RodilloPositivo,background
        =("#%02x%02x%02x" % (20,20,21))).place(
        x=425-300+XPMM, y =395+YPMM) # Boton flecha arriba 
        Button(self, image=self.BotonFlechaAbajo, 
        border="0", command=self.RodilloNegativo,background
        =("#%02x%02x%02x" % (20,20,21))).place(
        x=425-300+XPMM, y =495+YPMM) # Boton flecha abajo
        Button(self, image=self.BotonGrabar, 
        border="0", command=self.Grabar,background
        =("#%02x%02x%02x" % (20,20,21))).place(
        x=425+XPMM, y =495+YPMM) # Boton flecha abajo
# Espacio para Panel "Conexión":
    # Etiquetas:
        Label(self, image=self.PanelConexion,bg=("#%02x%02x%02x" 
        % (70,70,71))).place(x=18, y=0) # Panel y etiquetas
    # Menu de opciones:
        self.VarPuerto.set(self.MenuPuertosCom[0])
        OptionMenu(self,self.VarPuerto,*self.MenuPuertosCom).place(x=130,
        y=60) # Menú de puertos COM
        self.VarVelocidades.set(self.MenuVelocidades[0])
        OptionMenu(self,self.VarVelocidades,*self.MenuVelocidades).place(x=145,
        y=115) # Menú de velocidades
    # Botones:
        Button(self, image=self.BotonConectar, border="0", 
        command=self.ConectarArduino, # Botón conectar
        background=("#%02x%02x%02x" % (20,20,21))).place(x=50,y=190)
        Button(self, image=self.BotonDesconectar, border="0", 
        command=self.DesconectarArduino, # Botón desconectar
        background=("#%02x%02x%02x" % (20,20,21))).place(x=50,y=250)
        Button(self, image=self.BotonActualizar, border="0", 
        command=self.ActualizarPuerto, # Botón actualizar
        background=("#%02x%02x%02x" % (20,20,21))).place(x=50, y =310)
# Espacio para Panel "Archivo":
        XPA=360 # Posicion del panel en X
        YPA=10 # Posicion del panel en Y
    # Etiquetas:
        Label(self,image=self.PanelArchivo,border="0",bg=("#%02x%02x%02x"%
        (70,70,71))).place(x=XPA-15,y=YPA) # Panel y etiquetas
    # Campos de texto:
        self.CapturaTexto.set("Ingrese el texto a traducir...") # Captura de texto (lee el texto ingresado)
        self.campo=Entry(self,textvariable=self.CapturaTexto,
        font=("Console",15),fg="Light Gray")
        self.campo.bind('<Key-Return>',self.LeerCampo)
        self.campo.place(x=XPA+20,y=60+YPA)
    # Textos dezplasables:
        self.text_area = st.ScrolledText(self,width=60,height=8,font=("Console",10),
        fg="Gray") # Campo en el cual se muestran errores y parametros
        self.text_area.grid(column=0,pady=10,padx=10)
        self.text_area.place(x=XPA+20,y=230+YPA)
    # Botones:       
        Button(self,image=self.BotonAbrir,border="0",command=self.TraducirArchivo,background=
        ("#%02x%02x%02x" %(20,20,21))).place(x=0+XPA,y=110+YPA) # Botón abrir archivo
        Button(self, image=self.BotonTraducir,border="0", command=self.LeerCampo2,background=
        ("#%02x%02x%02x" % (20,20,21))).place(x=100+XPA,y=110+YPA) # Botón traducir
        Button(self, image=self.BotonImprimir,border="0", command=self.Imprimir,background=
        ("#%02x%02x%02x" % (20,20,21))).place(x=200+XPA,y=110+YPA) # Botón imprimir
        Button(self, image=self.BotonPrevisualizar,border="0", command=self.Previsualizar,background=
        ("#%02x%02x%02x" % (20,20,21))).place(x=300+XPA,y=110+YPA) # Botón previsualizar 
        Button(self, image=self.BotonEstado,border="0", command=self.Revisar,background=
        ("#%02x%02x%02x" % (20,20,21))).place(x=300+XPA,y=50+YPA) # Botón previsualizar 
        Button(self, image=self.BotonGuardar,border="0", command=self.Guardar,background=
        ("#%02x%02x%02x" % (20,20,21))).place(x=300+XPA,y=450+YPA) # Botón previsualizar 