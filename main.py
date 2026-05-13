#Elaborado por: Juan González
#Fecha de creación: 24/04/2026  Hora: 13:23
#Última modificación:
#Versión 3.14.3

#Importaciones
import funciones
reemplazos = []
#Definición de funciones
def submenu(opt,tokens,bitacora):
    if opt == 1:
        funciones.filtrarPorDia(bitacora)
        funciones.insertarBitacora(bitacora, "Se buscó en bitácora por fecha")
    elif opt == 2:
        funciones.filtrarPorPalabra(bitacora)
        funciones.insertarBitacora(bitacora, "Se buscó en bitácora por palabra clave")
    return ""
def menu(opt,tokens,bitacora):
    if opt == 1:
        nombreArchivo = input("Indique el nombre del archivo donde están almacenados los tokens, no escriba la extención del archivo: ")
        separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: "))
        while separador not in [1,2,3]:
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.cargarTokens(nombreArchivo,separador,tokens)
        funciones.insertarBitacora(bitacora, "Se cargó un archivo de tokens")
        return tokens
    elif opt == 2:
        funciones.insertarBitacora(bitacora, "Se mostraron los tokens")
        return funciones.mostrarTokens(tokens)
    elif opt == 3:
        nuevosTokens = input("Porfavor ingrese los nuevos tokens, utilize un punto '.' para separar cada token, y utilize un separador"
                             "entre el token y la equivalencia ('->', ',', '='): ")
        separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: "))
        while separador not in [1, 2, 3]:
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.agregarModificarTokens(separador, tokens, nuevosTokens,bitacora)
        return tokens
    elif opt == 4:
            funciones.guardarTokens(tokens)
            funciones.insertarBitacora(bitacora, "Se guardaron tokens en un archivo")
            return ""
    elif opt == 5:
        reemplazos = funciones.traducirCodigoAux(tokens)
        return "Traducción finalizada"
    elif opt == 6:
        funciones.generarCSV()
        funciones.insertarBitacora(bitacora, "Se generó un archivo CSV")
    elif opt == 7:
        return "7"
    elif opt == 8:
        opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                  "Porfavor digíte el número de la acción que desea realizar: "))
        while opt != 3:
            print(submenu(opt, tokens, bitacora))
            opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                "Porfavor digíte el número de la acción que desea realizar: "))
        return "8"
#Programa Principal
tokens = []
bitacora = funciones.cargarBitacora()
opt = int(input("Menú del sistema:\n1-Cargar tokens\n2-Mostrar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
            "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
            "Porfavor digíte el número de la acción que desea realizar: "))
while opt != 9:
    print(menu(opt,tokens,bitacora))
    opt = int(input("\nMenú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
          "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
          "Porfavor digíte el número de la acción que desea realizar: "))
funciones.insertarBitacora(bitacora, "El usuario salió del programa")
print("Programa Finalizado")