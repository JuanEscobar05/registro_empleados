# Ver todos los empleados

def ver_empleados(empleados):
    if not empleados:
        print('No hay usuarios registrados 👎')
        return
    
    for emp in empleados:
        salario = emp['horas'] * emp['valor_hora']
        print(f'Nombre: {emp['nombre']} | Cargo: {emp['cargo']} | salario: ${salario: .2f} ')
        print()