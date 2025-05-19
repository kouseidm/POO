class estudiante:
    def __init__ (self, codigo, nombre, curso, notaP, notaF):
        self.codigo = codigo
        self.nombre = nombre
        self.curso = curso
        self.notaP = notaP
        self.notaF = notaF
    def __str__ (self):
        return print(f"Alumno con codigo {self.codigo} y nombre {self.nombre}. En el curso {self.curso} saco en el parcial {self.notaP} y en el final {self.notaF}")
    def calcularNF(self):
        NotaF = (self.notaP * 0.4) + (self.notaF * 0.6)
        return round(NotaF, 2)
    def aprobo(self, a):
        aprobo = False
        if a >= 13:
            aprobo = True
        else:
            aprobo = False
        return print(f"El estudiante aprobo?: {aprobo}")


print("Bienvenido, ingrese sus datos:".center(30))
print("- - "*20)
cod = str(input("Ingrese el codigo del estudiante: "))
nom = str(input("Ingrese el nombre del estudiante: "))
cur = str(input("Ingrese el curso a calcular la nota: "))
Parcial = float(input("Ingrese la nota del examen parcial: "))
Final = float(input("Ingrese la nota del examen final: "))
estudiante1 = estudiante(cod, nom, cur, Parcial, Final)
estudiante1.__str__()
a = estudiante1.calcularNF()
print(f"La nota final es: {estudiante1.calcularNF()}")
estudiante1.aprobo(a)

