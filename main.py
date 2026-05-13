#Elaborado por: Juan González y Alessandro Arias
#Fecha de creación: 24/04/2026  Hora: 13:23
#Última modificación:
#Versión 3.14.3

#Importaciones
import funciones

#Definición de funciones
def submenu(opt,bitacora):
    """
    Funcionamiento: Ejecuta las opciones disponibles del submenú de bitácora.
    Entradas:
        opt (str): opción seleccionada por el usuario.
        bitacora(list): lista con los registros de acciones realizadas.
    Salidas: None.
    """
    if opt == "1":
        funciones.filtrarPorDia(bitacora)
        funciones.insertarBitacora(bitacora, "Se buscó en bitácora por fecha")
    elif opt == "2":
        funciones.filtrarPorPalabra(bitacora)
        funciones.insertarBitacora(bitacora, "Se buscó en bitácora por palabra clave")
def menu(opt,tokens,reemplazos,tiempo,bitacora):
    """
    Funcionamiento: Ejecuta las opciones principales del menú del sistema según la selección del usuario.
    Entradas:
        opt (str): opción seleccionada por el usuario.
        tokens (list): lista de tokens almacenados.
        reemplazos (list): lista de reemplazos realizados durante la traducción.
        tiempo (float): tiempo empleado en el proceso de traducción.
        bitacora (list): lista con los registros de acciones realizadas.
    Salidas:
        tuple: retorna tokens, reemplazos y tiempo actualizados.
    """
    if opt == "1":
        nombreArchivo = input("\nIndique el nombre del archivo .txt donde están almacenados los tokens: ")
        separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: ")
        while separador not in "123":
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.cargarTokens(nombreArchivo,separador,tokens)
        funciones.insertarBitacora(bitacora, "Se cargó un archivo de tokens")
    elif opt == "2":
        funciones.insertarBitacora(bitacora, "Se mostraron los tokens")
        print(funciones.mostrarTokens(tokens))
    elif opt == "3":
        nuevosTokens = input("\nPorfavor ingrese los nuevos tokens, puede utilizar los siguientes separadores de equivalencia: '->', ',' o '='.\n"
                             "Para separar equivalencias use un '.' \n(Ej. print=imprimir.input=entrada)\nIngrese los datos: ")
        separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: ")
        while separador not in "123":
            separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='")
        tokens = funciones.agregarModificarTokens(separador,tokens,nuevosTokens,bitacora)
    elif opt == "4":
        print(funciones.guardarTokens(tokens))
        funciones.insertarBitacora(bitacora, "Se guardaron tokens en un archivo")
        print("Se guardó el archivo .csv")
    elif opt == "5":
        reemplazos,tiempo = funciones.traducirCodigoAux(tokens)
        print("Proceso finalizada")
    elif opt == "6":
        print(funciones.generarCSV())
        funciones.insertarBitacora(bitacora, "Se generó un archivo CSV")
    elif opt == "7":
        titulo = input("Ingrese el título para el reporte HTML: ")
        print(funciones.generarHTML(titulo,reemplazos,tiempo,tokens))
    elif opt == "8":
        opt = input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n0-Salir\n"
                  "Porfavor digíte el número de la acción que desea realizar: ")
        while opt != "0":
            print(submenu(opt,bitacora))
            opt = input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n0-Salir\n"
                "Porfavor digíte el número de la acción que desea realizar: ")
    return tokens,reemplazos,tiempo
#Programa Principal
tokens = []
reemplazos = []
tiempo = 0.0
opt = input("Menú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
            "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n0-Salir\n"
            "Porfavor digíte el número de la acción que desea realizar: ")
while opt != "0":
    bitacora = funciones.cargarBitacora()
    tokens,reemplazos,tiempo = menu(opt,tokens,reemplazos,tiempo,bitacora)
    opt = input("\nMenú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
          "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n0-Salir\n"
          "Porfavor digíte el número de la acción que desea realizar: ")
funciones.insertarBitacora(bitacora, "El usuario salió del programa")
print("Programa Finalizado")