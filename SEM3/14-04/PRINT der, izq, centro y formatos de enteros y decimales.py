#numero
a = 123
print(f"|{a:25}|")
print(f"|{a:<25}|")
print(f"|{a:^25}|")


#texto
a = "123"
print(f"|{a:25}|")
print(f"|{a:>25}|")
print(f"|{a:^25}|")


#numeros enteros y decimales
variable = 100000
print(f"Esto imprime sin formatear {variable}")
print(f"Esto imprime con formato {variable:,d}")
print(f"Esto imprime con espaciado y formato {variable:10,d}\n")

variable = 1200356.8796
print(f"Con dos decimales: {variable:.2f}") # f=flotante, .2=dos decimales
print(f"Con cuatro decimales: {variable:.4f}") # f=flotante, .4=cuatro decimales
print(f"Con dos decimales y coma: {variable:,.2f}") # ,=formato con miles, millones