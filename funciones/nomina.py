# Ver nomina

def ver_nomina(empleados):
    total = sum(emp['horas'] * emp['valor_hora'] for emp in empleados)
    print(f' El total de la nomina es: ${total: .2f}')