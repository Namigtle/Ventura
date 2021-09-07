Estado = 'APBPCPDPEP'  # Arreglo de estados
PosicionLeva = [49, 57, 66, 73, 80, 0, 19, 25, 32, 42]  # Arreglo de posiciones angulares


def MoverDerercha(Direccion, Contador, ArregloCoor, Salidas):
    Direccion += 1  # Cambia a dirección positiva
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    # Agrega posicion de leva
    Salidas.append("G:" + str(PosicionLeva[Direccion]))
    #if not(ArregloCoor[Contador][1] >= ArregloCoor[Contador-1][1]):
    #Salidas.append("H")
    Salidas.append("C:" + str(ArregloCoor[Contador][0]) +
                   "," + str(ArregloCoor[Contador][1]))  # Agrega coordenada X y Y
    Direccion += 1  # Cambia a dirección positiva
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    # Agrega posicion de leva
    Salidas.append("G:" + str(PosicionLeva[Direccion]))
    return Direccion, Salidas  # regresa la direccion y el arreglo de salidas


def MoverIzquierda(Direccion, Contador, ArregloCoor, Salidas):
    Direccion -= 1  # Cambia a dirección negativa
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    Salidas.append("G:" + str(PosicionLeva[Direccion]))  # Agrega posicion leva
    #if not(ArregloCoor[Contador][1] >= ArregloCoor[Contador-1][1]):
    #Salidas.append("H")
    Salidas.append("C:" + str(ArregloCoor[Contador][0]) +
                   "," + str(ArregloCoor[Contador][1]))  # Agrega coordenada X y Y
    Direccion -= 1  # Cambia a direccion negativa
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    Salidas.append("G:" + str(PosicionLeva[Direccion]))  # Agrega posición leva
    return Direccion, Salidas  # Regrea la direccion y el arreglo de salidas


def NoMover(Direccion, Contador, ArregloCoor, Salidas):
    Direccion += 1  # Cambia a direccion positiva
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    Salidas.append("G:" + str(PosicionLeva[Direccion]))  # Agrega posicion leva
    #if not(ArregloCoor[Contador][1] >= ArregloCoor[Contador-1][1]):
    #Salidas.append("H")
    Salidas.append("C:" + str(ArregloCoor[Contador][0]) +
                   "," + str(ArregloCoor[Contador][1]))  # Agrega coordenada X y Y
    Direccion -= 1  # Cambia a direccion negativa
    if Direccion < 0:
        Direccion = 9
    elif Direccion > 9:
        Direccion = 0
    Salidas.append("G:" + str(PosicionLeva[Direccion]))
    return Direccion, Salidas  # Regrea la direccion y el arreglo de salidas


def NuevaFuncion(TextTraducido):
    ArregloEntradas = []  # Arreglo de entradas
    FlancoCoor = []  # Arreglo de boleanos
    IndexFC = False  # dato boleano
    for n in range(0, len(TextTraducido)):
        residuo = 0
        for m in range(0, len(TextTraducido[1])):
            if (TextTraducido[n][m] == 1):  # si existe un "1" en el texto traducido
                if m == 0:  # si el "1" esta en la posicion 0
                    # agrega "a" al ArregloEntradas
                    ArregloEntradas.append('a')
                elif m == 1:  # si el "1" esta en la posicion 1
                    # agrega "b" al ArregloEntradas
                    ArregloEntradas.append('b')
                elif m == 2:  # si el "1" esta en la posicion 2
                    # agrega "c" al ArregloEntradas
                    ArregloEntradas.append('c')
                FlancoCoor.append(IndexFC)
            else:
                residuo += 1
            if residuo == 3:  # si no existe un "1" en el texto traducido
                ArregloEntradas.append('0')  # agrega "0" al ArregloEntradas
                FlancoCoor.append(IndexFC)
        IndexFC = not IndexFC
    return ArregloEntradas, FlancoCoor


def EnviarDatos(TextTraducido, ArregloCoordenadas):
    ArregloEntradas = []  # Arreglo de entradas
    FlancoCoor = []
    ParametrosCodificados = []
    _Direccion = 0
    _Contador = 0
    Con = False
    ArregloEntradas, FlancoCoor = NuevaFuncion(TextTraducido)
    # Maquina de estados :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    for IndexAE in range(len(ArregloEntradas)):
        EstadoActual = Estado[_Direccion]
        conmutador = (FlancoCoor[IndexAE] or Con
                      ) and (not (FlancoCoor[IndexAE] and Con))
        if conmutador:
            _Contador += 1
            Con = not Con
    # CASO A :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (EstadoActual == 'A') & (ArregloEntradas[IndexAE] == 'a'):
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'A') & (ArregloEntradas[IndexAE] == 'b'):
            _Direccion, ParametrosCodificados = NoMover(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'A') & (ArregloEntradas[IndexAE] == 'c'):
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
    # CASO B :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (EstadoActual == 'B') & (ArregloEntradas[IndexAE] == 'a'):
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'B') & (ArregloEntradas[IndexAE] == 'b'):
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'B') & (ArregloEntradas[IndexAE] == 'c'):
            _Direccion, ParametrosCodificados = NoMover(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
    # CASO C :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (EstadoActual == 'C') & (ArregloEntradas[IndexAE] == 'a'):
            _Direccion, ParametrosCodificados = NoMover(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'C') & (ArregloEntradas[IndexAE] == 'b'):
            _Contador = _Contador - 1
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
            _Contador = _Contador + 1
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'C') & (ArregloEntradas[IndexAE] == 'c'):
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
    # CASO D :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (EstadoActual == 'D') & (ArregloEntradas[IndexAE] == 'a'):
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'D') & (ArregloEntradas[IndexAE] == 'b'):
            _Contador = _Contador - 1
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
            _Contador = _Contador + 1
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'D') & (ArregloEntradas[IndexAE] == 'c'):
            _Direccion, ParametrosCodificados = NoMover(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
    # CASO E :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (EstadoActual == 'E') & (ArregloEntradas[IndexAE] == 'a'):
            _Direccion, ParametrosCodificados = NoMover(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'E') & (ArregloEntradas[IndexAE] == 'b'):
            _Direccion, ParametrosCodificados = MoverDerercha(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
        elif (EstadoActual == 'E') & (ArregloEntradas[IndexAE] == 'c'):
            _Direccion, ParametrosCodificados = MoverIzquierda(
                _Direccion, _Contador, ArregloCoordenadas, ParametrosCodificados)
    return ParametrosCodificados


def ObtenerXY(Cadena):
    Dato = []
    for item in range(len(Cadena)):
        if (Cadena[item][0] == 'C'):
            Seccion1 = Cadena[item].split(':')[1]
            Dato.append(Seccion1.split(','))
    return Dato


"""	IndexFC = False
	for n in range(0,len(TextTraducido)):
		residuo = 0
		for m in range(0,len(TextTraducido[1])):
			if (TextTraducido[n][m] == 1):
				if m == 0:
					ArregloEntradas.append('a')
				elif m == 1:
					ArregloEntradas.append('b')
				elif m == 2:
					ArregloEntradas.append('c')
				FlancoCoor.append(IndexFC)
			else:
				residuo = residuo + 1
			if residuo == 3:
				ArregloEntradas.append('0')
				FlancoCoor.append(IndexFC)
		IndexFC = not IndexFC"""
