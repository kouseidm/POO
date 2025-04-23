x = "El tercer campeonato mundial de fútbol fue en 1938"
y = "El cuarto campeonato mundial de fútbol fue en 1950"

anio1 = x[-4::1]
anio2 = y[-4::1]

print (anio1)
print (anio2)

anio1 = int(anio1)
anio2 = int(anio2)

if anio1 > anio2:
    dif = anio1-anio2
else:
    dif = anio2 - anio1
print("Han pasado ",dif, " años.")