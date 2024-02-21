from pila import Pila

# Creación de instancias de las pilas
PILA_CARACTER = Pila()
PILA_CLAVE = Pila()

# Conjuntos de elementos clave de inicio y final
ELEMENTOS_CLAVE_INICIO = {'(', '['}
ELEMENTOS_CLAVE_FINAL = {')', ']'}

respuesta: str = ''  # Variable global para almacenar respuestas

def leer_entrada_usuario_o_prueba(prueba_texto: str | None = None) -> list[str]:
    """
    Lee la entrada del usuario o la entrada de prueba y realiza las operaciones necesarias en las pilas.

    Args:
        o (str | None): El texto de prueba proporcionado para la entrada de prueba. None si se espera entrada del usuario.

    Returns:
        list[str]: Una lista de respuestas que indica las operaciones realizadas en las pilas.
    """
    # Obtener el texto de entrada del usuario o de la prueba
    texto: str = '' 
    if prueba_texto is None:
        texto = str(input("Indroduzca un carácter:  \n >>"))
        while len(texto:=texto.strip())==0:
            texto = str(input("Indroduzca un carácter:  \n >>"))
    else:
        texto = prueba_texto

    respuestas: list[str] = []
    # Procesar cada carácter en el texto de entrada
    for caracter in texto:
        if caracter in ELEMENTOS_CLAVE_INICIO:
            # Si el carácter es un elemento clave de inicio, se agrega a la pila de claves
            PILA_CLAVE.push(caracter)
            respuestas.append(f"Se ha ingresado el carácter: '{caracter}' a la pila")
        elif caracter in ELEMENTOS_CLAVE_FINAL: 
            # Si el carácter es un elemento clave de final
            if PILA_CLAVE.estaVacia():
                # Si la pila de claves está vacía, se genera un error
                respuestas.append("Error: No se puede ingresar un carácter de cierre ya que la pila está vacía")
            elif (caracter == ')' and PILA_CLAVE.top() == '(') or (caracter == ']' and PILA_CLAVE.top() == '['):
                # Si el carácter coincide con el elemento de apertura correspondiente en la cima de la pila, se extrae
                respuestas.append(f"Se ha extraido el carácter: '{PILA_CLAVE.top()}' de la pila")
                PILA_CLAVE.pop()
                
            else:
                # Si el carácter de cierre no coincide con el elemento de apertura correspondiente, se genera un error
                respuestas.append("Error: El carácter ingresado no es válido")
        else:
            # Si el carácter no es un elemento clave, se agrega a la pila de caracteres
            PILA_CARACTER.push(caracter)
            respuestas.append(f"Se ha ingresado el carácter: '{caracter}' a la pila de carácteres")
    
    return respuestas

def main():
    """
    Función principal del programa para equilibrar símbolos.
    """
    print("Equilibrado de Símbolos")
    while True:
        respuestas: list[str] = leer_entrada_usuario_o_prueba()

        # Salir del programa (código comentado)
        # if respuestas == SALIR:
        #     print("Ha finalizado la ejecución del programa")
        #     PILA_CLAVE.borrar_pila()
        #     break

        # Imprimir respuestas y estado de las pilas
        print(respuestas)
        print(f"Pila Clave: {PILA_CLAVE}")
        print(f"Pila Carácter: {PILA_CARACTER}")

if __name__ == '__main__':
    main()
