from ejercicio_pila import leer_entrada_usuario_o_prueba

def ejecutar_pruebas(pruebas: list[tuple], mensaje_error: str) -> None:
    """
    Ejecuta una serie de pruebas y verifica si las respuestas obtenidas coinciden con las esperadas.

    Args:
        pruebas (list[tuple]): Una lista de tuplas donde cada tupla contiene el texto de entrada y las respuestas esperadas.
        mensaje_error (str): El mensaje de error a mostrar si una prueba falla.

    Returns:
        None
    """
    print("Equilibrado de Símbolos")
    print(f'Prueba: {pruebas}')

    respuestas_esperadas: list[str] = []
    respuestas_obtenidas: list[str] = []
    for prueba in pruebas:
        texto, mensajes = prueba
        respuestas_esperadas = mensajes
        respuestas_obtenidas = leer_entrada_usuario_o_prueba(texto)

        prueba_exitosa = all(esperada == obtenida for esperada, obtenida 
                         in zip(respuestas_esperadas, respuestas_obtenidas))
        if not prueba_exitosa:
            print(respuestas_esperadas)
            print(respuestas_obtenidas)
            raise ValueError(mensaje_error)

def correr_prueba_pila_elemento_no_clave() -> None:
    """
    Ejecuta una prueba para verificar el comportamiento de la pila cuando se ingresa un elemento no clave.

    Raises:
        ValueError: Si la prueba falla.
    """
    PRUEBA = [
        ("a", ["Se ha ingresado el carácter: 'a' a la pila de carácteres"])
    ]
    ejecutar_pruebas(PRUEBA, "Error: Prueba de pila con elemento no clave, valor inesperado")

def correr_prueba_pila_vacia() -> None:
    """
    Ejecuta una prueba para verificar el comportamiento de la pila cuando está vacía.

    Raises:
        ValueError: Si la prueba falla.
    """
    PRUEBA = [
        (")", ["Error: No se puede ingresar un carácter de cierre ya que la pila está vacía"])
    ]
    ejecutar_pruebas(PRUEBA, "Error: Prueba de pila vacía, valor inesperado")

def correr_prueba_pila_elementos_clave_inicio() -> None:
    """
    Ejecuta una prueba para verificar el comportamiento de la pila con elementos clave de inicio.

    Raises:
        ValueError: Si la prueba falla.
    """
    PRUEBA = [
        ("(", ["Se ha ingresado el carácter: '(' a la pila"]),
        ("[", ["Se ha ingresado el carácter: '[' a la pila"]),
    ]
    ejecutar_pruebas(PRUEBA, "Error: Prueba de pila con elementos clave de inicio, valor inesperado")

def correr_prueba_pila_elementos_clave_final() -> None:
    """
    Ejecuta una prueba para verificar el comportamiento de la pila con elementos clave de final.

    Raises:
        ValueError: Si la prueba falla.
    """
    PRUEBA = [
        ("(", ["Se ha ingresado el carácter: '(' a la pila"]),
        ("[", ["Se ha ingresado el carácter: '[' a la pila"]),
        ("]", ["Se ha extraido el carácter: '(' de la pila"]),
        (")", ["Se ha extraido el carácter: '[' de la pila"]),
    ]
    ejecutar_pruebas(PRUEBA, "Error: Prueba de pila con elementos clave de final, valor inesperado")

def correr_prueba_pila_elementos_clave_final_invalida() -> None:
    """
    Ejecuta una prueba para verificar el comportamiento de la pila con elementos clave de final inválidos.

    Raises:
        ValueError: Si la prueba falla.
    """
    PRUEBA = [
        ("(", ["Se ha ingresado el carácter: '(' a la pila"]),
        ("[", ["Se ha ingresado el carácter: '[' a la pila"]),
        (")", ["Error: El carácter ingresado no es válido"]),
        ("]", ["Se ha extraido el carácter: '(' de la pila"]),
    ]
    ejecutar_pruebas(PRUEBA, "Error: Prueba de pila con elementos clave de final inválidos, valor inesperado")

def main():
    """
    Función principal para ejecutar todas las pruebas.
    """
    correr_prueba_pila_vacia()
    correr_prueba_pila_elementos_clave_inicio()
    correr_prueba_pila_elementos_clave_final()
    correr_prueba_pila_elementos_clave_final_invalida()

if __name__ == '__main__':
    main()
