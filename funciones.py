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
def cargarTokens(nombreArchivo,separador,tokens):
    # token = tuple()
    if separador == 1:
        separador = " -> "
    elif separador == 2:
        separador = ", "
    elif separador == 3:
        separador = "="
    archivo = open(f"{nombreArchivo}.txt", "r")
    for line in archivo:                            #Lee cada línea del archivo
        token = line.strip().split(separador)       #Crea una lista con el token y la equivalencia
        if not validarToken(token):
            print(f"El token '{token}' no es válido")
        else:
            token = (token[0], token[1])  # Pase de una lista a una tupla
            for x in tokens:  # Lee cada equivalencia ya guardada en la lista de tokens
                if x[0] == token[0]:  # Si el nuevo token ya existe, imprime que se va a reescribir
                    print(f"Se reescribió el token '{token[0]}'")
                    x = token
            tokens.append(token)
    archivo.close()
    return tokens