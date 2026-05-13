#Elaborado por: Juan González
#Fecha de creación: 24/04/2026  Hora: 13:23
#Última modificación:
#Versión 3.14.3

#Importaciones
import funciones

#Definición de funciones
def submenu(opt,tokens):
    if opt == 1:
        return "A"
    elif opt == 2:
        return "B"
def menu(opt,tokens,reemplazos,tiempo):
    if opt == "1":
        nombreArchivo = input("Indique el nombre del archivo .txt donde están almacenados los tokens: ")
        separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: ")
        while separador not in "123":
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.cargarTokens(nombreArchivo,separador,tokens)
    elif opt == "2":
        print(funciones.mostrarTokens(tokens))
    elif opt == "3":
        nuevosTokens = input("Porfavor ingrese los nuevos tokens, utilize un punto '.' para separar cada token, y utilize un separador"
                             "entre el token y la equivalencia ('->', ',', '='): ")
        separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: ")
        while separador not in "123":
            separador = input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='")
        tokens = funciones.agregrarModificarTokens(separador, tokens, nuevosTokens)
    elif opt == "4":
        return "4"
    elif opt == "5":
        reemplazos,tiempo = funciones.traducirCodigoAux(tokens)
        print("Traducción finalizada")
    elif opt == "6":
        return "6"
    elif opt == "7":
        titulo = input("Ingrese el título para el reporte HTML: ")
        print(funciones.generarHTML(titulo,reemplazos,tiempo,tokens))
    elif opt == "8":
        opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                  "Porfavor digíte el número de la acción que desea realizar: "))
        while opt != 3:
            print(submenu(opt))
            opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                "Porfavor digíte el número de la acción que desea realizar: "))
    return tokens,reemplazos,tiempo
#Programa Principal
tokens = []
reemplazos = []
tiempo = 0.0
opt = input("Menú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
            "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n0-Salir\n"
            "Porfavor digíte el número de la acción que desea realizar: ")
while opt != "0":
    tokens,reemplazos,tiempo = menu(opt,tokens,reemplazos,tiempo)
    opt = input("\nMenú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
          "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
          "Porfavor digíte el número de la acción que desea realizar: ")
print("Programa Finalizado")