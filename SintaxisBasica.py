# en pytthon no es necesario declarar tipo de dato
#reales float double
# float 32 bits , significado de 32 bits es que se almacenan en 32 bits "reserva de memoria"
# reales double 64 bit, significado de 64 bit es que se almacena en 64 bit
"""
floatfloat numero = 3.14
double numero = 3.1489
"""

#enteros int
#booleanos bool
#string str

"""
tipos de condiciones
if
elif
else
casos -> match apartir de la version 3.10
ojo con las versiones de python, porque las versiones inferiores no son compatibles
con algunas sintaxis de versiones superiores
"""

"""
ciclos ciclicos -> ciclos de repeticion
for = para
while = mientras
break = romper # palabras reserv
continue = continuar # palabras reservadas en python
pass = no hacer nada
"""

if True:
    print("hola mundo true")
edad= 18 
if edad >= 18:
    print("Eres mayor de edad")
else: # se ejecuta si la condicion es falsa
    print("Eres menor de edad") # se ejecuta si la condicion es falsa
    
# condicionales compuestos
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
#condiciones anidadas o multiples

print(" segun el numero es el rol que va a mostrar")
opcion= int(input("ingrese el numero de opcion: ")) 
if opcion == 1:
    print("opcion 1 administrador")
if opcion == 2:
    print("opcion 2 usuario")
if opcion == 3:
    print("opcion 3 aprendiz")
else:
    print("opcion no valida")
    
    
if opcion == 1: 
    print("el rol es administrador")
else:
    if opcion == 2:
        print("el rol es usuario")
    else:
        if opcion == 3:
            print("el rol es apremdiz")
        else:
            print("el rol no existe")