from pila import Pila

PILA = Pila()
SALIR = 's'
ELEMENTOS_CLAVE_INICIO = {'(','['}
ELEMENTOS_CLAVE_FINAL = {')',']'}

respuesta: str = ''

def leer_entrada_usuario_o_prueba(prueba_caracter: str | None = None) -> str:
    caracter: str = '' 
    if prueba_caracter is None:
        caracter = str(input("Indroduzca un carácter:  \n >>"))
        while not len(caracter:=caracter.strip())==1:
            caracter = str(input("Indroduzca un carácter:  \n >>"))
    else:
        caracter: str = prueba_caracter

    if str(caracter).lower() == SALIR:
        return caracter
    elif caracter in ELEMENTOS_CLAVE_INICIO:
        PILA.push(caracter)
        return f"Se ha ingresado el carácter: '{caracter}' a la pila"
    elif caracter in ELEMENTOS_CLAVE_FINAL: 
        if PILA.estaVacia():
            return "Error: No se puede ingresar un carácter de cierre ya que la pila está vacía"

        if ( caracter == ')' and PILA.top() == '(') or (caracter == ']' and PILA.top() == '['):
            PILA.pop()
            return f"Se ha extraido el carácter: '{PILA.top()}' de la pila"

        return "Error: El carácter ingresado no es válido"
    
    return "El carácter no es un elemento clave"

def main():
    print("Equilibrado de Símbolos")
    print(f'Ingrese el carácter "{SALIR}" para terminar la ejecución del progarama')
    while True:
        respuesta = leer_entrada_usuario_o_prueba()

        if respuesta == SALIR:
            print("Ha finalizado la ejecución del programa")
            PILA.borrar_pila()
            break

        print(respuesta)
        print(f"Pila: {PILA}")

if __name__ == '__main__':
    main()