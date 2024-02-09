
print('                     \033[32mCalificaciones de estudiantes de actuaría UTECA\033[0m')
class Estudiante:
    def __init__(self, matricula, nombre, edad):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

class EstudianteGraduado(Estudiante):
    def __init__(self, matricula, nombre, edad):
        super().__init__(matricula, nombre, edad)
        self.fechagraduacion = None
        self.tesis = None

    def graduarse(self):
        promedio_final = self.obtener_promedio()
        return promedio_final >= 6.0

    def set_fecha_tesis(self, fecha, nombretesis):
        self.fechagraduacion = fecha
        self.tesis = nombretesis

