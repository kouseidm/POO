 
radianes= float(input("Ingrese un angulo en radianes"))
angsexag= radianes * 100/ 3.141592 #123.123214
grados= int(angsexag) #123
aux1 = (angsexag - grados) * 60 # 0.123214 * 60 = 7.39284
minutos = int(aux1)
aux2 = (aux1 - minutos) *60 # 0.39284 * 60 = 23.5704
segundos = int(aux2)

print("angulo: ", grados, " - ",  minutos, " - ", segundos)

