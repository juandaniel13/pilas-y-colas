class Pila:
    PILA_VACIA: str = "La pila se encuentra vacía"

    def __init__(self) -> None:
        """Inicializa una nueva pila vacía."""
        self.caracteres: list[str] = []
        
    def push(self, X: str) -> None:
        """
        Agrega un elemento a la parte superior de la pila.

        Args:
            X (str): El elemento a agregar a la pila.

        Returns:
            None
        """
        self.caracteres.append(X)

    def pop(self) -> str | None:
        """
        Elimina y devuelve el elemento en la parte superior de la pila.

        Returns:
            str | None: El elemento eliminado de la pila, o None si la pila está vacía.
        """
        try:
            return self.caracteres.pop()
        except IndexError:
            print(Pila.PILA_VACIA)
            return None

    def estaVacia(self) -> bool:
        """
        Comprueba si la pila está vacía.

        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return self.caracteres == []

    def top(self) -> str:
        """
        Devuelve el elemento en la parte superior de la pila sin eliminarlo.

        Returns:
            str: El elemento en la parte superior de la pila.
        """
        try:
            return self.caracteres[-1]
        except IndexError:
            print(Pila.PILA_VACIA)
            return None

    def borrar_pila(self) -> None:
        """
        Elimina todos los elementos de la pila.

        Returns:
            None
        """
        self.caracteres.clear()

    def __str__(self) -> str:
        """
        Devuelve una representación de cadena de la pila.

        Returns:
            str: Una representación de cadena de la pila.
        """
        return '[' + ', '.join(self.caracteres) + ']'
