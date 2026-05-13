#Elaborador por: Juan González y Alessandro Arias
#Fecha de creación: 24/04/2026  Hora: 13:37
#Última modificacíón:
#Versión 4.14.3

#Importación de librerías
import re
from datetime import datetime
import pickle
import csv
#Definición de funciones
#Cargar tokens
def validarToken(token):
    """
    Funcionamiento: Verifica si un token inicia con caracteres alfabéticos válidos.
    Entradas: token (list).
    Salidas: bool (True si el token es válido, False en caso contrario).
    """
    if re.match('[A-Za-z]', token[0] and token[1]):
        return True
    return False
def escogerSeparador(separador):
    """
    Funcionamiento: Convierte la opción numérica seleccionada por el usuario en su separador correspondiente.
    Entradas: separador (str).
    Salidas: str (separador seleccionado).
    """
    if separador == "1":
        separador = "->"
    elif separador == "2":
        separador = ","
    elif separador == "3":
        separador = "="
    return separador
def cargarTokens(nombreArchivo,separador,tokens):
    """
    Funcionamiento: Carga tokens desde un archivo de texto y los almacena en la lista de tokens.
    Entradas:
        nombreArchivo (str): nombre del archivo sin extensión.
        separador (str): opción del separador seleccionado.
        tokens (list): lista de tokens ya existentes.
    Salidas: list (tokens actualizados).
    """
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
    """
    Funcionamiento: Agrega nuevos tokens o modifica los existentes según los datos ingresados por el usuario.
    Entradas:
        separador (str): opción del separador seleccionado.
        tokens (list): lista actual de tokens.
        nuevosTokens (str): cadena con los nuevos tokens.
        bitacora (list): lista de registros de acciones.
    Salidas: list (tokens actualizados o tokens originales si no se guardan los cambios).
    """
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
    aceptar = input("Desea guardar los cambios realizados? Escoja una opción:\n1-Sí\n2-No\nDigíte su respuesta: ")
    while aceptar not in "12":
        aceptar = input("Desea guardar los cambios realizados? Escoja una opción:\n1-Sí\n2-No\nDigíte su respuesta: ")
    if aceptar == "1":
        return tokens
    return tokensAntiguos
#Mostrar tokens
def mostrarTokens(tokens):
    """
    Funcionamiento: Muestra en pantalla todos los tokens almacenados.
    Entradas: tokens (list).
    Salidas: str (retorna cadena vacía).
    """
    if len(tokens) == 0:
        print("No hay tokens cargados.")
    else:
        print("Tokens Cargados hasta el momento:")
        for original, equivalencia in tokens:
            print(f"{original} -> {equivalencia}")
    return ""
#Traducir código
def validarTokens(llaves, tokens):
    """
    Funcionamiento: Verifica cuáles llaves encontradas coinciden con tokens válidos.
    Entradas:
        llaves (list): lista de palabras encontradas.
        tokens (list): lista de tokens registrados.
    Salidas: list o bool (lista de coincidencias o False si no existen).
    """
    temp = []
    for x in llaves:
        for y in tokens:
            if x[0] == y[0]:
                temp.append(x)
    if len(temp) > 0:
        return temp
    return False
def cambiarToken(token,tokens):
    """
    Funcionamiento: Busca un token y retorna su equivalencia correspondiente.
    Entradas:
        token (str): token a reemplazar.
        tokens (list): lista de tokens registrados.
    Salidas: str (equivalencia encontrada).
    """
    for x in tokens:
        if x[0] == token:
            token = x[1]
            break
    return token
def contarReemplazos(reemplazos, llaves):
    """
    Funcionamiento: Cuenta cuántas veces se reemplaza cada token.
    Entradas:
        reemplazos (list): lista de reemplazos realizados.
        llaves (list): lista de tokens encontrados.
    Salidas: list (reemplazos actualizados).
    """
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
def compararReemplazosTokens(reemplazos,tokens):
    """
    Funcionamiento: Compara los reemplazos realizados con la lista total de tokens.
    Entradas:
        reemplazos (list): lista de reemplazos realizados.
        tokens (list): lista de tokens registrados.
    Salidas: list (reemplazos completados con tokens no utilizados).
    """
    for x in tokens:
        cambia = False
        for y in reemplazos:
            if x[0] == y[0]:
                cambia = True
                break
        if cambia == False:
            reemplazos.append([x[0], 0])
    return reemplazos
def traducirLinea(line, llaves, tokens):
    """
    Funcionamiento: Traduce una línea de texto reemplazando los tokens encontrados.
    Entradas:
        line (str): línea original.
        llaves (list): lista de coincidencias encontradas.
        tokens (list): lista de tokens registrados.
    Salidas: str (línea traducida).
    """
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
    """
    Funcionamiento: Traduce el contenido de un archivo utilizando los tokens registrados.
    Entradas:
        archivo (str): archivo original.
        nArchivo (str): archivo donde se guardará la traducción.
        tokens (list): lista de tokens registrados.
    Salidas: tuple (reemplazos realizados y tiempo de ejecución).
    """
    reemplazos = []
    llaves = []
    tiempo = 0.0
    try:
        cronometroI = datetime.now()
        f = open(archivo, "r")
        g = open(nArchivo, "a")
        for line in f:
            for llave in re.finditer(r"[A-Za-z0-9]+", line):        #Expresión regular para encontrar datos alfanuméricos
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
                reemplazos = compararReemplazosTokens(reemplazos, tokens)
                traduccion = traducirLinea(line, llaves, tokens)
                g.write(traduccion)
            llaves = []
        f.close()
        g.close()
        cronometroF = datetime.now()
        tiempo = cronometroF - cronometroI
    except:
        print(f"No se encuentra el archivo {archivo}")
    return reemplazos,tiempo
def traducirCodigoAux(tokens):
    """
    Funcionamiento: Solicita los archivos necesarios y ejecuta la traducción del código.
    Entradas: tokens (list).
    Salidas: tuple (resultado de la traducción).
    """
    archivo = input("Introduzca el archivo a traducir, indique la extensión: ")
    nArchivo = input("Introduzca el nombre del archivo donde desea guardar la traducción, indique la extensión (Ej. traduccion.txt): ")
    reemplazos = traducirCodigo(archivo, nArchivo, tokens)
    return reemplazos
def guardarTokens(tokens):  #Se eligió porque es una forma simple y rápida de guardar los datos sin necesidad de hacer cálculos adicionales.
    """
    Funcionamiento: Guarda los tokens en un archivo de texto utilizando un separador seleccionado por el usuario.
    Entradas: tokens (list).
    Salidas: str (retorna cadena vacía).
    """
    if len(tokens) == 0:
        print("No hay tokens para guardar.")
        return
    nombreArchivo = input("Indique el nombre del nuevo archivo donde desea guardar los tokens: ")
    separador = input("Indique el separador que desea usar:\n1-'->'\n2-','\n3-'='\nOpción: ")
    while separador not in "123":
        separador = input("Indique el separador que desea usar:\n1-'->'\n2-','\n3-'='\nOpción: ")
    separador = escogerSeparador(separador)
    with open(f"{nombreArchivo}.txt", "w") as archivo:
        for original, equivalencia in tokens:
            archivo.write(f"{original} {separador} {equivalencia}\n")
    return "Tokens guardados correctamente."
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
    return "Reporte CSV generado correctamente."
def insertarBitacora(bitacora, descripcion):
    """
    Funcionamiento: Agrega un nuevo registro a la bitácora con fecha y hora actual y guarda los datos en un archivo.
    Entradas: bitacora (list), descripcion (str).
    Salidas: None.
    """
    fechaHora = datetime.now()
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
#Reporte HTML
def sumarReemplazos(reemplazos):
    """
    Funcionamiento: Calcula la cantidad total de reemplazos realizados.
    Entradas: reemplazos (list).
    Salidas: int (suma total de reemplazos).
    """
    suma = 0
    for x in reemplazos:
        suma += x[1]
    return suma
def sacarPorcentajeReemplazos(reemplazos):
    """
    Funcionamiento: Calcula el porcentaje de palabras que fueron reemplazadas.
    Entradas: reemplazos (list).
    Salidas: float (porcentaje de reemplazos).
    """
    palabras = 0
    cambios = 0
    for x in reemplazos:
        palabras += 1
        if x[1] != 0:
            cambios += 1
    porcentaje = (cambios*100)/palabras
    return porcentaje
def crearTabla(reemplazos,tokens):
    """
    Funcionamiento: Genera el código HTML de una tabla con los reemplazos realizados.
    Entradas:
        reemplazos (list): lista de reemplazos.
        tokens (list): lista de tokens registrados.
    Salidas: str (tabla HTML generada).
    """
    tabla = """"""
    for x in reemplazos:
        token = x[0]
        reemplazos = x[1]
        for i in tokens:
            if token == i[0]:
                reemplazo = i[1]
                break
        temp = f"""
                <tr>
                    <td>{token}</td>
                    <td>{reemplazo}</td>
                    <td>{reemplazos}</td>
                  </tr>
                """
        tabla += temp
    return tabla
def generarHTML(titulo,reemplazos,tiempo,tokens):
    """
    Funcionamiento: Genera un reporte HTML con información sobre la traducción realizada.
    Entradas:
        titulo (str): título del reporte.
        reemplazos (list): lista de reemplazos realizados.
        tiempo (str): duración del proceso.
        tokens (list): lista de tokens registrados.
    Salidas: str (mensaje de confirmación con el nombre del archivo generado).
    """
    fecha = datetime.now()
    fecha = fecha.strftime("%d-%m-%Y_%H-%M-%S")
    nombreArchivo = f"reporteHTML_{fecha}.html"
    sumaReemplazos = sumarReemplazos(reemplazos)
    porcentaje = sacarPorcentajeReemplazos(reemplazos)
    tabla = crearTabla(reemplazos,tokens)
    formato = f"""
            <!DOCTYPE html>
            <html>
            <head>
              <title>{titulo}</title>
              <style>
                body {{background-color: antiquewhite;display: flex;justify-content: center;align-items: center;text-align: center;flex-direction: column;min-height: 100px;margin: 0;}}
                th, td {{border: 1px solid #ccc;padding: 8px 16px;}}
                tr:nth-child(odd) {{background-color: #ffffff;}}
                tr:nth-child(even) {{background-color: #f2f2f2;}}
                table {{border-collapse: collapse; margin-top: 1rem;}}
              </style>
            </head>
            <body>
                <h1>Reporte de Traducción</h1>
                <h2>{fecha}</h2>
                <p>Duración del proceso: {tiempo}</p>
                <p>Total de reemplazos: {sumaReemplazos}</p>
                <p>Porcentaje de palabras reemplazadas: %{porcentaje}</p>
                <table>
                  <tr><th colspan="3">Tabla de tokens</th></tr>
                  <tr>
                    <th>Palabra Original</th>
                    <th>Reemplazo</th>
                    <th>Cantidad de Reemplazos</th>
                  </tr>
                  {tabla}
                </table>
            </body>
            </html>
            """
    with open(nombreArchivo, "a") as f:
        f.write(formato)
    return f"Reporte HTML generado con el nombre {nombreArchivo}"