class ticket:
    def _init_(self,costo,hora):
        self.__costo = costo
        self.__hora = hora 
    
    #METODO DE ACCESO
    def get_costo(self):
        return self.__costo
    def set_costo(self,costo):
        self.__costo = costo
    
    def get_hora(self):
        return self.__hora
    def set_hora(self, hora):
        self.__hora = hora
    #fin metodo de aceso

    def mostrar_ticket(self):
        print(f"Ticket {self.get_costo} --> {self.get_hora}")
    def NocheHora(self):
        hora = int(self.get_hora[:2])
        if 18<= hora <= 23:
            return True
        else:
            print("La hora esta fuera de rango")
            return False
ticket1 = ticket(10, 18)
ticket1.mostrar_ticket()


    #FALTA - completar
