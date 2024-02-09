from lib import *

def tabla(estudiante):
    tabla = f"|{'Matrícula':^10}|{'Nombre':^25}|{'Edad':^5}|{'Calificaciones':^20}|{'Promedio Final':^15}|{'Graduado':^10}|{'Fecha Graduación':^15}|{'Nombre Tesis':^30}|"
    tabla += "\n" + "-" * 135
    tabla += f"\n|{estudiante.matricula:^10}|{estudiante.nombre:^25}|{estudiante.edad:^5}|"
    
    for calificacion in estudiante.calificaciones:
        color = 'red' if calificacion <= 5 else 'black'
        tabla += f"\033[38;2;255;0;0m{calificacion:^4}\033[0m" if color == 'red' else f"\033[38;2;0;0;0m{calificacion:^4}\033[0m"

    promedio = estudiante.obtener_promedio()
    colorpromedio = '\033[48;2;255;0;0m' if promedio <= 5.9 else '\033[48;2;255;255;255m'
    tabla += f"|{promedio:^15}{colorpromedio}|"

    graduado = 'Si' if isinstance(estudiante, EstudianteGraduado) and estudiante.graduarse() else 'No'
    tabla += f"{graduado:^10}|"

    fechagraduación = estudiante.fechagraduacion if estudiante.fechagraduacion else 'N/A'
    nombretesis = estudiante.tesis if estudiante.tesis else 'N/A'
    tabla += f"{fechagraduación:^15}|{nombretesis:^30}|"

    return tabla

def información(estudiante):
    texto = f"\nInformación de {estudiante.nombre}:"
    texto += f"Nombre completo: {estudiante.nombre} Edad: {estudiante.edad} Matrícula: {estudiante.matricula} "

    if isinstance(estudiante, EstudianteGraduado):
        graduado = 'Sí' if estudiante.graduarse() else 'No'
        texto += f"¿Se gradúa? {graduado} "

        if estudiante.graduarse():
            texto += f"Fecha de graduación: {estudiante.fechagraduacion} "
            texto += f"Nombre de la tesis: {estudiante.tesis}"
        else:
            texto += "Estudiante No Graduado"

    return texto

if __name__ == "__main__":
    estudiante1 = EstudianteGraduado("601049", "Zaira Acosta", 35)
    estudiante1.agregar_calificacion(10)
    estudiante1.agregar_calificacion(9)
    estudiante1.agregar_calificacion(8)
    estudiante1.agregar_calificacion(10)
    estudiante1.agregar_calificacion(9)

    if isinstance(estudiante1, EstudianteGraduado):
        estudiante1.set_fecha_tesis("01/07/2013", "Los neutrinos saben a jugo de Uvas")
        
    estudiante2 = EstudianteGraduado("601048", "Durán frine", 34)
    estudiante2.agregar_calificacion(6)
    estudiante2.agregar_calificacion(5)
    estudiante2.agregar_calificacion(5)
    estudiante2.agregar_calificacion(4)
    estudiante2.agregar_calificacion(3)

    if isinstance(estudiante2, EstudianteGraduado):
        estudiante2.set_fecha_tesis("N/A", "N/A")
    print(tabla(estudiante1))
    print(tabla(estudiante2))
    print(información(estudiante1))
    print(información(estudiante2))


