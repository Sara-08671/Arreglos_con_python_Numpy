print("segun el numero es el rol que deba mostrar")
opcion=int(input("ingrese el numero de opcion:"))

match opcion:
    case 1:
        print("es el rol de administrador")
    case 2:
        print("es el rol de usuario")
    case 3:
        print("es el rol de cliente")
    case _:
        print("no se encotro el rol")