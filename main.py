#Menú navegación

from funciones.registrar import registrar_empleado, empleados
from funciones.ver import ver_empleados
from funciones.nomina import ver_nomina
from funciones.eliminar import eliminar_empleado

while True:
    print(' ====== MENÚ PRINCIPAL ====== ')
    print(' 1. Registrar Usuarios')
    print(' 2. Ver todos los empleados')
    print(' 3. ver total nomina')
    print(' 4. Eliminar empleado por id')
    print(' 5. Salir')

    opcion = int(input('Ingresa la opción correspondiente: '))

    if opcion == 1:
        registrar_empleado()
    elif opcion == 2:
        ver_empleados(empleados)
    elif opcion == 3:
        ver_nomina(empleados)
    elif opcion == 4:
        eliminar_empleado(empleados)
    elif opcion == 5:
        print('saliendo del programa 👋👋👋')
        break
    else:
        print('Opción incorrecta')