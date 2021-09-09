from tabla_de_transicion import *

while True:
    print()
    print('Bienvenido al programa de tabla de transiciones'.center(200, '*'))
    print('1. Mostrar tabla de transiciones')
    print('2. Modificar tabla de transiciones')
    print('3. Ver grafo generado')
    print('4. salir')
    opcion = int(input('Ingrese una opcion: '))
    print()
    tabla = Tabla('Tabla-transiciones.xlsx')
    
    if opcion == 1:
        print('Tabla de transiciones'.center(100, '-'))
        print()
        tabla.cargarTabla()
    elif opcion == 2:
        print('Opcion 2')
    elif opcion == 3:
            print('Opcion 3')
    elif opcion == 4:
        exit()
    else:
        print('Opcion incorrecta, fin del programa')
        