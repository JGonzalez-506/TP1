#Elaborador por: Juan González y Alessandro Arias
#Fecha de creación: 24/04/2026  Hora: 13:37
#Última modificacíón:
#Versión 4.14.3

#Definición de funciones
#Cargar tokens
def validarToken(token):
    import re
    if re.match('[A-Za-z]', token[0] and token[1]):
        return True
    return False
def escogerSeparador(separador):
    if separador == 1:
        separador = "->"
    elif separador == 2:
        separador = ","
    elif separador == 3:
        separador = "="
    return separador
def cargarTokens(nombreArchivo,separador,tokens):
    separador = escogerSeparador(separador)
    archivo = open(f"{nombreArchivo}.txt", "r")
    for line in archivo:                            #Lee cada línea del archivo
        token = line.strip().split(separador)       #Crea una lista con el token y la equivalencia
        token[0],token[1] = token[0].strip(),token[1].strip()
        repetido = False
        if validarToken(token):
            token = (token[0], token[1])  # Pase de una lista a una tupla
            for indice, pos in enumerate(tokens):  # Lee cada equivalencia ya guardada en la lista de tokens
                if pos[0] == token[0]:  # Si el nuevo token ya existe, imprime que se va a reescribir
                    print(f"Se reescribió el token de '{token[0]}'")
                    tokens[indice] = token
                    repetido = True
            if not repetido:
                tokens.append(token)
        else:
            print(f"El token '{token}' no es válido")
    archivo.close()
    return tokens
#Agregar o modificar tokens
def agregrarModificarTokens(separador,tokens,nuevosTokens):
    tokensAntiguos = tokens.copy()
    separador = escogerSeparador(separador)
    nuevosTokens = nuevosTokens.split(".")
    for token in nuevosTokens:
        token = token.strip().split(separador)  # Crea una lista con el token y la equivalencia
        token[0], token[1] = token[0].strip(), token[1].strip()
        repetido = False
        if validarToken(token):
            token = (token[0], token[1])             # Pase de una lista a una tupla
            for indice, pos in enumerate(tokens):  # Lee cada equivalencia ya guardada en la lista de tokens
                if pos[0] == token[0]:              # Si el nuevo token ya existe, imprime que se va a reescribir
                    print(f"Se reescribió el token de '{token[0]}'")
                    tokens[indice] = token
                    repetido = True
            if not repetido:
                print(f"Se añadió el token de '{token}'")
                tokens.append(token)
        else:
            print(f"El token '{token}' no es válido")
    print()
    aceptar = int(input("Desea guardar los cambios realizados? Escoja una opción:\n1-Sí\n2-No\nDigíte su respuesta: "))
    while aceptar not in [1, 2]:
        aceptar = int(input("Desea guardar los cambios realizados? Escoja una opción:\n1-Sí\n2-No\nDigíte su respuesta: "))
    if aceptar == 1:
        return tokens
    return tokensAntiguos
#Mostrar tokens
def mostrarTokens(tokens):
    if len(tokens) == 0:
        print("No hay tokens cargados.")
    else:
        print("Tokens Cargados hasta el momento:")
        for original, equivalencia in tokens:
            print(f"{original} -> {equivalencia}")
    return ""
#Traducir código
def validarTokens(llaves, tokens):
    temp = []
    for x in llaves:
        for y in tokens:
            if x[0] == y[0]:
                temp.append(x)
    if len(temp) > 0:
        return temp
    return False
def cambiarToken(token,tokens):
    for x in tokens:
        if x[0] == token:
            token = x[1]
            break
    return token
def contarReemplazos(reemplazos, llaves):
    for x in llaves:
        if reemplazos != []:
            repetido = False
            for y in reemplazos:
                if y[0] == x[0]:
                    y[1] += 1
                    repetido = True
            if repetido == False:
                reemplazos.append([x[0], 1])
        else:
            reemplazos.append([x[0], 1])
    return reemplazos
def traducirLinea(line, llaves, tokens):
    indice = 0
    primera = True
    traduccion = ""
    for x in range(len(llaves)):
        cambioAct = llaves[indice]
        token = cambioAct[0]
        equivalencia = cambiarToken(token,tokens)
        inicio = cambioAct[1]
        fin = cambioAct[2]
        if indice < len(llaves)-1:
            cambioSig = llaves[indice + 1]
            sig = cambioSig[1]
            indice += 1
        else:
            sig = fin
        if primera:
            traduccion += line[:inicio] + equivalencia + line[fin:sig]
            primera = False
        else:
            traduccion += equivalencia + line[fin:sig]
    traduccion += line[fin:len(line)]
    return traduccion
def traducirCodigo(archivo, nArchivo, tokens):
    import re
    reemplazos = []
    llaves = []
    f = open(archivo, "r")
    g = open(nArchivo, "a")
    for line in f:
        for llave in re.finditer(r"[A-Za-z0-9]+", line):
            temp = []
            temp.append(llave.group())
            temp.append(llave.start())
            temp.append(llave.end())
            llaves.append(temp)
        llaves = validarTokens(llaves, tokens)
        if llaves == False:
            print("No hay reemplazos por hacer.")
            g.write(line)
        else:
            reemplazos = contarReemplazos(reemplazos, llaves)  # Cuenta las veces que se cambia una palabra
            traduccion = traducirLinea(line, llaves, tokens)
            g.write(traduccion)
        llaves = []
    f.close()
    g.close()
    return reemplazos
def traducirCodigoAux(tokens):
    archivo = input("Introduzca el archivo a traducir, indique la extensión: ")
    nArchivo = input("Introduzca el nombre del archivo donde desea guardar la traducción, no escriba ninguna extensión: ")
    nArchivo += ".txt"
    reemplazos = traducirCodigo(archivo, nArchivo, tokens)
    return reemplazos