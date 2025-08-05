"""_summary_
    
    ciclo for recorrido ascendente y descendente
"""

print("__________________ejemplo ascendente__________________")
# region ciclo for recorrido ascendente
for i in range(1,11):
    print(i)
#endregion
    
print("__________________ejemplo descendente__________________")
#region ciclo for recorrido descendente 
for i in range(10,0,-1):
    print(i)
#endregion
    
#region intervalo 2
print("__________________intervalo de 2__________________")
for i in range(11,-1,-2):
    print(i)
#endregion
#region deletrear for
#internamente python que lo que hace, la variable tiene la palabra

"""_summary_
"""
variable = "Hola mundo"
longitud=len(variable)
for i in variable: #variable en esta estructura varifica longitud
    valor=i
    print("palabra", valor)