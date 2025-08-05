#medicina de ejecucion
import time
import os,sys
inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecución:", tiempoFinal)

time.sleep(5) #Pausa 2 segundos
if sys.platform == "win32":
    os.system('cls') #limpia la consola en windows
else:
    os.system('clear') #limpia la consola en Unix/linux

#Ciclo mientras 
inicio =time.time()
contador=0 
while contador <= 10:
    print(contador)
    contador +=1 #contador = contador +1
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecución", tiempoFinal)
"""
   contador = contador +1
   0 = 0 + 1
   1 = 1 + 1
   2 = 2 + 1
   3 = 3 + 1
   4 = 4 + 1...
"""