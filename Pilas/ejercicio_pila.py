from pila import Pila

PILA_CARACTER = Pila()
PILA_CLAVE = Pila()
ELEMENTOS_CLAVE_INICIO = {'(','['}
ELEMENTOS_CLAVE_FINAL = {')',']'}

respuesta: str = ''

def leer_entrada_usuario_o_prueba(prueba_texto: str | None = None) -> list[str]:
    texto: str = '' 
    if prueba_texto is None:
        texto = str(input("Indroduzca un carácter:  \n >>"))
        while len(texto:=texto.strip())==0:
            texto = str(input("Indroduzca un carácter:  \n >>"))
    else:
        texto = prueba_texto

    respuestas: list[str] = []
    for caracter in texto:
        if caracter in ELEMENTOS_CLAVE_INICIO:
            PILA_CLAVE.push(caracter)
            respuestas.append(f"Se ha ingresado el carácter: '{caracter}' a la pila")
        elif caracter in ELEMENTOS_CLAVE_FINAL: 
            if PILA_CLAVE.estaVacia():
                respuestas.append("Error: No se puede ingresar un carácter de cierre ya que la pila está vacía")

            if ( caracter == ')' and PILA_CLAVE.top() == '(') or (caracter == ']' and PILA_CLAVE.top() == '['):
                PILA_CLAVE.pop()
                respuestas.append(f"Se ha extraido el carácter: '{PILA_CLAVE.top()}' de la pila")

            respuestas.append("Error: El carácter ingresado no es válido")
        else:
            PILA_CARACTER.push(caracter)
            respuestas.append(f"Se ha ingresado el carácter: '{caracter}' a la pila de carácteres")
    
    return respuestas

def main():
    print("Equilibrado de Símbolos")
    while True:
        respuestas: list[str] = leer_entrada_usuario_o_prueba()

        # if respuestas == SALIR:
        #     print("Ha finalizado la ejecución del programa")
        #     PILA_CLAVE.borrar_pila()
        #     break

        print(respuestas)
        print(f"Pila Clave: {PILA_CLAVE}")
        print(f"Pila Carácter: {PILA_CARACTER}")

if __name__ == '__main__':
    main()