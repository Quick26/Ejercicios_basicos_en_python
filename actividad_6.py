#Hector Emiliano Llamas Salinas - 02997840

#Ejercicio 1
#Creamos dos cadenas, una con nombre y otra con apellido
#Asignamos las cadenas a las variables nombre y apellido respectivamente
#Concatenamos ambas variables e imprimimos el resultado usando print()
nombre = "Emiliano"
apellido = "Llamas"
print(nombre+ " " +apellido)




#Ejercicio 2
# Declara un objeto de la clase Bar()
# muestra el carácter del atributo "fill" hasta lograr el 100%
# Durante el proceso se escribe un archivo de texto con 
# 5000 caracteres ('B' y 'A') que son generados por una función aleatoria para generar una sensacion de tiempo real
from progress.bar import Bar, ChargingBar
import os, time, random
pro="Progreso:"
print(pro)
bar3 = Bar(fill='#--', suffix='%(percent)d%% ') 
caracteres = ['B', 'A']
datos = os.getcwd()+os.sep+"datos.txt"
archivo = open(datos, "w")
for i in range(0,100):
    cadena = " "
    longitud = 50000
    for num in range(longitud):
        cadena += caracteres[random.randint(0, 1)]
    
    archivo.write(cadena + "\n")
    bar3.next()
    
bar3.finish()
archivo.close
