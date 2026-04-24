#Elaborado por: Juan González
#Fecha de creación: 24/04/2026  Hora: 13:23
#Última modificación:
#Versión 3.14.3

#Definición de funciones
def menu(opt):
    if opt == 1:
        return "1"
    elif opt == 2:
        return "2"
    elif opt == 3:
        return "3"
    elif opt == 4:
        return "4"
    elif opt == 5:
        return "5"
    elif opt == 6:
        return "6"
    elif opt == 7:
        return "7"
    elif opt == 8:
        return "8"

#Programa Principal
opt = int(input("Menú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
            "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
            "Porfavor digíte el número de la acción que desea realizar: "))
while opt != 9:
    print(menu(opt))
    opt = int(input("Menú del sistema:\n1-Cargar tokens\n2-Mostar tokens\n3-Agregar/modificar tokens\n4-Guardar tokens\n"
          "5-Traducir código\n6-Generar CSV\n7-Generar HTML\n8-Submenú de bitácora del sistema\n9-Salir\n"
          "Porfavor digíte el número de la acción que desea realizar: "))
print("Programa Finalizado")