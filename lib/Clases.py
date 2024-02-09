
print('                     \033[32mCalificaciones de estudiantes de actuaría UTECA\033[0m')
class Estudiante:
    def __init__(self, matricula, nombre, edad):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregarcalificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def obtenerpromedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

class EstudianteGraduado(Estudiante):
    def __init__(self, matricula, nombre, edad):
        super().__init__(matricula, nombre, edad)
        self.fechagraduacion = None
        self.tesis = None

    def graduarse(self):
        promedio_final = self.obtenerpromedio()
        return promedio_final >= 6.0

    def setfechatesis(self, fecha, nombretesis):
        self.fechagraduacion = fecha
        self.tesis = nombretesis

