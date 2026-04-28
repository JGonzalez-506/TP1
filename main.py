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
def menu(opt,tokens):
    if opt == 1:
        nombreArchivo = input("Indique el nombre del archivo donde están almacenados los tokens, no escriba la extención del archivo: ")
        separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: "))
        while separador not in [1,2,3]:
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.cargarTokens(nombreArchivo,separador,tokens)
        return tokens
    elif opt == 2:
        return "2"
    elif opt == 3:
        nuevosTokens = input("Porfavor ingrese los nuevos tokens, utilize un punto '.' para separar cada token, y utilize un separador"
                             "entre el token y la equivalencia ('->', ',', '='): ")
        separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='\nOpción: "))
        while separador not in [1, 2, 3]:
            separador = int(input("Indique el separador utilizado:\n1-'->'\n2-','\n3-'='"))
        tokens = funciones.agregrarModificarTokens(separador, tokens, nuevosTokens)
        return tokens
    elif opt == 4:
        return "4"
    elif opt == 5:
        return "5"
    elif opt == 6:
        return "6"
    elif opt == 7:
        return "7"
    elif opt == 8:
        opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                  "Porfavor digíte el número de la acción que desea realizar: "))
        while opt != 3:
            print(submenu(opt))
            opt = int(input("\nSubmenú del sistema:\n1-Acciones por día escogido\n2-Acciones con algunas palabras clave\n3-Salir\n"
                "Porfavor digíte el número de la acción que desea realizar: "))
        return "8"

#Programa Principal
tokens = []
opt = int(input("Menú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
            "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
            "Porfavor digíte el número de la acción que desea realizar: "))
while opt != 9:
    print(menu(opt,tokens))
    opt = int(input("\nMenú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
          "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
          "Porfavor digíte el número de la acción que desea realizar: "))
print("Programa Finalizado")