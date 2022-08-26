print ("-----------------------------------------------------------------")
print ("ejercicio 13 empleados, sueldo mayor pagina 198")
print ("-----------------------------------------------------------------")

#entradas
print ("ingrese la cantidad de empleados:")
ce = int(input())

#inicializar
i = 1
smayor = 0.0  #inicializando real

#proceso
print ("ingrese los sueldos")
while i <= ce:
    sueldo = float(input("ingrese sueldo {0}:".format(i)))

if sueldo > smayor:
    smayor = sueldo
c = i
i = i+1



#salida
print("el empleado numero ",c, "tiene el mayor sueldo que es: ",smayor)