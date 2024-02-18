from Estructuras import Pila

print("Equilibrado de símbolos")
pila = Pila()
while True: 
    print('Ingrese la palabra "salir" para terminar la ejecución del progarama')
    userInput = input("Indroduzca un carácter:  \n")
    userInput = userInput.strip() #elimina los espacios en blanco
    if userInput in {'(','['}:
        print(f"se ha ingresado el carácter: '{userInput}' a la pila")
        pila.push(userInput)
    elif userInput in {')',']'}: 
        if pila.isEmpty():
            print("Error: No se puede ingresar un carácter de cierre ya que la pila está vacía ")
        else: 
            if ( userInput == ')' and pila.top() == '(') or (userInput == ']' and pila.top() == '['):
                print(f"se ha extraido el carácter: '{pila.top()}' de la pila")
                pila.pop()
            else:
                print("Error: El carácter ingresado no es válido")
            
    if userInput.lower() == "salir":
        print("Se ha terminado la ejecución del programa")
        break
    