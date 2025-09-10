#eliminar usuario por id

def eliminar_empleado(empleados):
    id_empleado = int(input('Ingrese el id del usuario a eliminar: '))
    for emp in empleados:
        if emp['id'] == id_empleado:
            empleados.remove(emp)
            print('Empliado eliminado con exito')
            return
        else:
            print('id incorrecto ')