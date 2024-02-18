while True: 
    print('Ingrese la palabra "salir" para terminar la ejecución del progarama')
    userInput = input("Indroduzca un caracter:  \n")
    userInput = userInput.strip() #elimina los espacios en blanco
    if userInput in {'(','['} and len(userInput) == 1:
        print("hola")
    if userInput.lower() == "salir":
        print("Se ha terminado la ejecución del programa")
        break
    else: 
        print(f"se ha ingresado el caracte: {userInput}")