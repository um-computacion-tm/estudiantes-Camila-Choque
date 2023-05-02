class Persona:
    def __init__(self, param_nombre, param_email, param_legajo):
        self.nmombre = param_nombre
        self.email = param_email
        self.legajo = param_legajo
        self.asistencia = 0
    
    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def asistencia_clase(self):
        self.asistencia += 1
    
class Profesor(Persona): 
    def __init__(self, param_nombre, param_email, param_legajo):
        self.legajo = param_legajo
        self.nombre = param_nombre
        self.email = param_email
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, param_legajo):
        self.legajo = param_legajo
        self.nmombre = param_nombre
        self.email = param_email
        super().__init__(param_nombre, param_email, param_legajo)

alumno_Marcos  = Alumno("Marcos", "marcos@gmail", "124532")
print("ALumno")
print(alumno_Marcos)
print("El nombre es: ")
print(alumno_Marcos.nmombre)
print("El email es: ")
print(alumno_Marcos.email)
print("El legajo es:")
print(alumno_Marcos.legajo)


profesor_pepe:Profesor = Profesor("Pepe","Jose@")
print(id(profesor_pepe))
print("El nombre es:")
print(profesor_pepe.nombre)
print("el mail es: ")
print(profesor_pepe.email)
print("su legajo es: ")
print(profesor_pepe.legajo)
print("Su asistencia es: ")
print(profesor_pepe.asistencia)

print("El profesor fue a clase..")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su ausencia es: ")
print(profesor_pepe.asistencia)
