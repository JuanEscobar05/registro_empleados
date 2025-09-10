#Función registrar empleado

empleados = []

def registrar_empleado():
    empleado = {}

    empleado['id'] = int(input('Ingrese su id: '))
    empleado['nombre'] = input( 'Ingrese su nombre: ')
    empleado['correo'] = input('Ingrese su correo: ')
    empleado['telefono'] = input('Ingrese su telefono: ')
    empleado['valor_hora'] = float(input('Ingrese el valor de hora: '))
    empleado['horas'] = float(input('Ingrese el valor de las horas trabajadas: '))
    empleado['cargo'] = input('Ingrese su cargo: ')

    empleados.append(empleado)

    print(' El usuario fue creado exitosamente 👍')
    return empleados
