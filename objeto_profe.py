class Profesor: 
    def __init__(self, param_nombre, param_email, param_legajo):
        self.nombre = param_nombre
        self.email = param_email
        self.legajo = param_legajo
        self.asistencia = 0
     
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def asistencia_clase(self):
        self.asistencia += 1
    
profesor_pepe = Profesor("Pepe","Jose@", "12563")
print(id(profesor_pepe))
print("El nombre es:")
print(profesor_pepe.nombre)
print("el email es: ")
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

