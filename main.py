from lib import *

def tabla(estudiante):
    tabla = f"|{'Matrícula':^10}|{'Nombre':^25}|{'Edad':^5}|{'Calificaciones':^20}|{'Promedio Final':^15}|{'Graduado':^10}|{'Fecha Graduación':^15}|{' Tesis':^30}|"
    tabla += "\n" + "-" * 135
    tabla += f"\n|{estudiante.matricula:^10}|{estudiante.nombre:^25}|{estudiante.edad:^5}|"
    
    for calificacion in estudiante.calificaciones:
        color = 'red' if calificacion <= 5 else 'black'
        tabla += f"\033[38;2;255;0;0m{calificacion:^4}\033[0m" if color == 'red' else f"{calificacion:^4}"

    promedio = estudiante.obtenerpromedio()
    colorpromedio = '' if promedio <= 5.9 else ''
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
print('                     \033[32mCalificaciones de estudiantes de actuaría UTECA\033[0m')

if __name__ == "__main__":
    estudiante1 = EstudianteGraduado("601049", "Zaira Acosta", 35)
    estudiante1.agregarcalificacion(10)
    estudiante1.agregarcalificacion(9)
    estudiante1.agregarcalificacion(8)
    estudiante1.agregarcalificacion(10)
    estudiante1.agregarcalificacion(9)

    if isinstance(estudiante1, EstudianteGraduado):
        estudiante1.setfechatesis("01/07/2013", "Los neutrinos saben a jugo de Uvas")
    #Primer Alumno   
    estudiante2 = EstudianteGraduado("601048", "Durán frine", 34)
    estudiante2.agregarcalificacion(6)
    estudiante2.agregarcalificacion(5)
    estudiante2.agregarcalificacion(5)
    estudiante2.agregarcalificacion(4)
    estudiante2.agregarcalificacion(3)

    if isinstance(estudiante2, EstudianteGraduado):
        estudiante2.setfechatesis("N/A", "N/A")
    #Segundo Alumno        
    estudiante3 = EstudianteGraduado("100738", "Garcia Victor", 20)
    estudiante3.agregarcalificacion(8)
    estudiante3.agregarcalificacion(3)
    estudiante3.agregarcalificacion(4)
    estudiante3.agregarcalificacion(5)
    estudiante3.agregarcalificacion(4)

    if isinstance(estudiante3, EstudianteGraduado):
        estudiante3.setfechatesis("N/A", "N/A")
    #Tercer Alumno
    estudiante4 = EstudianteGraduado("100744", "Lopez Diego", 20)
    estudiante4.agregarcalificacion(10)
    estudiante4.agregarcalificacion(9)
    estudiante4.agregarcalificacion(8)
    estudiante4.agregarcalificacion(10)
    estudiante4.agregarcalificacion(8)

    if isinstance(estudiante4, EstudianteGraduado):
        estudiante4.setfechatesis("05/01/2026", "N/A")
    #Cuarto Alimno
    estudiante5 = EstudianteGraduado("100692", "Lopez Evelyn", 20)
    estudiante5.agregarcalificacion(10)
    estudiante5.agregarcalificacion(8)
    estudiante5.agregarcalificacion(9)
    estudiante5.agregarcalificacion(5)
    estudiante5.agregarcalificacion(9)
    if isinstance(estudiante5, EstudianteGraduado):
         estudiante5.setfechatesis("05/01/2027", "N/A")

    #Quinto Alumno
    estudiante6 = EstudianteGraduado("99999", "Rojas Daniel", 20)
    estudiante6.agregarcalificacion(6)
    estudiante6.agregarcalificacion(5)
    estudiante6.agregarcalificacion(4)
    estudiante6.agregarcalificacion(4)
    estudiante6.agregarcalificacion(3)

    if isinstance(estudiante6, EstudianteGraduado):
        estudiante6.setfechatesis("N/A", "N/A")
    #Sexto Alumno
    estudiante7 = EstudianteGraduado("100870", "Rosas Maurizio", 20)
    estudiante7.agregarcalificacion(10)
    estudiante7.agregarcalificacion(6)
    estudiante7.agregarcalificacion(10)
    estudiante7.agregarcalificacion(9)
    estudiante7.agregarcalificacion(8)

    if isinstance(estudiante7, EstudianteGraduado):
        estudiante7.setfechatesis("08/01/2026", "N/A")
    #Septimo Alumno
    estudiante8 = EstudianteGraduado("100437", "Villegas Annibal", 20)
    estudiante8.agregarcalificacion(10)
    estudiante8.agregarcalificacion(5)
    estudiante8.agregarcalificacion(7)
    estudiante8.agregarcalificacion(8)
    estudiante8.agregarcalificacion(10)

    if isinstance(estudiante8, EstudianteGraduado):
        estudiante8.setfechatesis("12/01/2026", "N/A")
    #Octavo Alumno
print(tabla(estudiante1))
print(tabla(estudiante2))
print(tabla(estudiante3))
print(tabla(estudiante4))
print(tabla(estudiante5))
print(tabla(estudiante6))
print(tabla(estudiante7))
print(tabla(estudiante8))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('                               \033[36mDatos estudiantes de actuaría UTECA\033[0m')
print(información(estudiante1))
print(información(estudiante2))
print(información(estudiante3))
print(información(estudiante4))
print(información(estudiante5))
print(información(estudiante6))
print(información(estudiante7))
print(información(estudiante8))


