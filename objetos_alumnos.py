

class Alumno:
    def __init__(self, param_nombre, param_legajo, param_carrera, param_año, param_email): 

        self.nombre = param_nombre
        self.legajo = param_legajo
        self.carrera = param_carrera
        self.año = param_año
        self.email = param_email
    
    def cambiar_año(self, nuevo_año):
        self.año = nuevo_año
    
alumno_Marcos = Alumno ("Marcos", "62069", "Informatica","2", "marcos@gmail.com") 
print(id(alumno_Marcos))
print("El nombre es: ")
print(alumno_Marcos.nombre)
print("EL legajo es: ")
print(alumno_Marcos.legajo)
print("Su carrera es: ")
print(alumno_Marcos.carrera)
print("Su año es: ")
print(alumno_Marcos.año)  #preguntar 
print("El email es: ")
print(alumno_Marcos.email)

class Persona:
    def __init__(self, param_nombre, param_email, param_legajo):
        self.nmombre = param_nombre
        self.email = param_email
        self.legajo = param_legajo
        






