import numpy
from numpy import log   #En caso de necesitar otra función, se añade
                        #separando por una coma

x1 = 1      #Extremo inferior
x2 = 2      #Extremo superior
e = 0.0001  #Error o tolerancia
a = x2 - x1
n=int((log(a)-log(e))/log(2))

f_x = lambda x: x**3 + x - 5  #Función matemática a analizar

#Encabezado de la tabla, cada número después del acento circunflexo
#indica los espacios de la tabla, posteriormente se hace un margen 
print("{:^5}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","x1",
 "x2","f(x1)","f(x2)","xm","f(xm)")) 
print("-"*64)

#Inicio del ciclo, f_x indica a numpy que se debe evaluar la función
#matemática para imprimirla en los datos de salida

for i in range(0,n):
    xm=(x1+x2)/2
    fx1=f_x(x1)
    fx2=f_x(x2)
    fxm=f_x(xm) 
    
    print("{:^3}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(i,round(x1,5),
    round(x2,5),round(fx1,5),round(fx2,5),round(xm,5), round(abs(fxm),5)))
#Condicionales que debe cumplir la bisección
    if (fxm * fx1 < 0):
        x2 = xm
    else:
        x1 = xm
        
print("")
print("La solución por el método de bisección es: ",xm)

