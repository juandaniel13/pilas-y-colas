class Cola:
    """
    Representa una cola de elementos.
    """

    COLA_VACIA: str = "La cola se encuentra vacía"

    def __init__(self) -> None:
        """
        Inicializa una nueva cola vacía.
        """
        self.datos: list[tuple[bool, int, str]] = []
        
    def queue(self, X: tuple[bool, int, str]) -> None:
        """
        Encola un elemento en la cola.

        Args:
            X (tuple[bool, int, str]): El elemento a encolar.
        """
        self.datos.append(X)

    def dequeue(self) -> str | None:
        """
        Desencola un elemento de la cola.

        Returns:
            str | None: El elemento desencolado, o None si la cola está vacía.
        """
        try:
            return self.datos.pop(0)
        except IndexError:
            print(Cola.COLA_VACIA)

    def esta_vacia(self) -> bool:
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si la cola está vacía, False de lo contrario.
        """
        return self.datos == []

    def tam(self) -> int:
        """
        Obtiene el tamaño de la cola.

        Returns:
            int: El número de elementos en la cola.
        """
        return len(self.datos)

    def borrar_pila(self) -> None:
        """
        Borra todos los elementos de la cola.
        """
        for dato in self.datos:
            del dato
        del self.datos    

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la cola.

        Returns:
            str: Una cadena que representa la cola.
        """
        cola_str: str = '['
        for dato in self.datos:
            cola_str += f'{dato}, '
        return cola_str + ']'
