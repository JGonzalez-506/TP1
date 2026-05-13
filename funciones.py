#Elaborador por: Juan González y Alessandro Arias
#Fecha de creación: 24/04/2026  Hora: 13:37
#Última modificacíón:
#Versión 4.14.3

#Definición de funciones
#Cargar tokens
import datetime
import pickle
import csv
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
def agregarModificarTokens(separador,tokens,nuevosTokens,bitacora):
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
                    insertarBitacora(bitacora, f"Se modificó el token {token[0]}")
                    tokens[indice] = token
                    repetido = True
            if not repetido:
                print(f"Se añadió el token de '{token}'")
                insertarBitacora(bitacora, f"Se añadió el token {token[0]}")
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
        return ""
    else:
        print("Tokens Cargados hasta el momento separados por ->:")
        for original, equivalencia in tokens:
            print(f"{original} -> {equivalencia}")
    return ""
def guardarTokens(tokens):
    """
    Funcionamiento: Guarda los tokens en un archivo de texto utilizando un separador seleccionado por el usuario.
    Entradas: tokens (list).
    Salidas: str (retorna cadena vacía).
    """
    if len(tokens) == 0:
        print("No hay tokens para guardar.")
        return
    nombreArchivo = input("Indique el nombre del nuevo archivo donde desea guardar los tokens: ")
    separador = int(input("Indique el separador que desea usar:\n1-'->'\n2-','\n3-'='\nOpción: "))
    while separador not in [1,2,3]:
        separador = int(input("Indique el separador que desea usar:\n1-'->'\n2-','\n3-'='\nOpción: "))
    separador = escogerSeparador(separador)
    with open(f"{nombreArchivo}.txt", "w") as archivo:
        for original, equivalencia in tokens:
            archivo.write(f"{original} {separador} {equivalencia}\n")
    print("Tokens guardados correctamente.")
    return ""
def generarCSV():
    """
    Funcionamiento: Permite al usuario ingresar datos de reemplazos y genera un archivo CSV con esa información.
    Entradas: No recibe parámetros (los datos se solicitan al usuario mediante input).
    Salidas: None (crea un archivo .csv con los datos ingresados).
    """
    reemplazos = []
    try:
        cantidad = int(input("¿Cuántos reemplazos desea ingresar? "))
    except ValueError:
        print("Cantidad inválida")
        return
    for i in range(cantidad):
        original = input("Digite la palabra original: ")
        reemplazo = input("Digite el reemplazo: ")
        try:
            veces = int(input("Digite la cantidad de reemplazos realizados: "))
        except ValueError:
            print("Cantidad inválida")
            return
        reemplazos.append((original, reemplazo, veces))
    nombreArchivo = input("Digite el nombre del archivo CSV: ")
    with open(f"{nombreArchivo}.csv", "w", newline="", encoding="utf-8") as archivoCSV: # Abre el archivo CSV para escritura y asegura que se maneje bien el salto de línea y los caracteres diferentes
        escritor = csv.writer(archivoCSV)
        escritor.writerow(["Palabra Original", "Reemplazo", "Cantidad"])
        for original, reemplazo, cantidad in reemplazos:
            escritor.writerow([original, reemplazo, cantidad])
    print("Reporte CSV generado correctamente.")
def insertarBitacora(bitacora, descripcion):
    """
    Funcionamiento: Agrega un nuevo registro a la bitácora con fecha y hora actual y guarda los datos en un archivo.
    Entradas: bitacora (list), descripcion (str).
    Salidas: None.
    """
    fechaHora = datetime.datetime.now()
    fechaHora = fechaHora.strftime("%Y-%m-%d_%H:%M:%S")
    registro = (fechaHora, descripcion)
    bitacora.append(registro)
    with open("bitacora.txt", "ab") as archivo:
        pickle.dump(bitacora, archivo)
def cargarBitacora():
    """
    Funcionamiento: Carga la bitácora desde un archivo si existe, o crea una lista vacía en caso contrario.
    Entradas: Ninguna.
    Salidas: list (bitacora).
    """
    try:
        with open("bitacora.txt", "rb") as archivo:
            bitacora = pickle.load(archivo)
    except:
        bitacora = []
    return bitacora
def filtrarPorDia(bitacora):
    """
    Funcionamiento: Muestra los registros de la bitácora que coinciden con una fecha específica ingresada por el usuario.
    Entradas: bitacora (list).
    Salidas: None.
    """
    fecha = input("Digite la fecha a buscar (AAAA-MM-DD): ")
    encontrados = False
    for fechaHora, descripcion in bitacora:
        if fechaHora.startswith(fecha):
            print(f"{fechaHora} -> {descripcion}")
            encontrados = True
    if not encontrados:
        print("No se encontraron registros para esa fecha.")
def filtrarPorPalabra(bitacora):
    """
    Funcionamiento: Muestra los registros de la bitácora que contienen una palabra clave ingresada por el usuario.
    Entradas: bitacora (list).
    Salidas: None.
    """
    palabra = input("Digite la palabra clave a buscar: ").lower()
    encontrados = False
    for fechaHora, descripcion in bitacora:
        if palabra in descripcion.lower():
            print(f"{fechaHora} -> {descripcion}")
            encontrados = True
    if not encontrados:
        print("No se encontraron coincidencias.")