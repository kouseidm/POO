n = int(input("INTRODUCE N: "))

for i in range(n+1):
    print("*"*(n-i))
    
for i in range(n+1):
    espacios = n-i
    print(" "*espacios + "*"*i)
