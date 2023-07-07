import numpy
from numpy import sin

x1=0 #Valor inicial
x2=1 #Valor final
e=0.0001 #Error o tolerancia
n=3 #Número de iteraciones 

#Recordar que el valor absoluto de la función evaluada en xrf
#Debe ser menor al error, por eso se va modificando el número de iteraciones

f_x = lambda x: sin(x) + x -1 #Función a analizar
#Encabezado de tabla
print("{:^5}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","x1",
 "x2","f(x1)","f(x2)","xrf","f(xrf)"))
#Margen de tabla
print("-"*65)
#Ciclo
for i in range (0,n):
    fx1=f_x(x1)
    fx2=f_x(x2)
    xrf=(x1*fx2-x2*fx1)/(fx2-fx1)
    fxrf=f_x(xrf)
    
    print("{:^3}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(i,round(x1,4),
    round(x2,4),round(fx1,4), round(fx2,4),round(xrf,4),round(abs(fxrf),4)))
                                                           
    if fxrf*fx1<0:
        x2=xrf
    else:
        x1=xrf

print("")
print("La solución por el método de regla falsa es: ", xrf)