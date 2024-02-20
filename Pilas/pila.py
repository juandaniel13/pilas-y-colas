class Pila:
    PILA_VACIA: str = "La pila se encuentra vacía"

    def __init__(self) -> None:
        self.caracteres: list[str] = []
        
    def push(self, X: str) -> None:
         self.caracteres.append(X)

    def pop(self) -> str | None:
        try:
            return self.caracteres.pop()
        except IndexError:
            print(Pila.PILA_VACIA)

    def estaVacia(self) -> bool:
        return self.caracteres == []

    def top(self) -> str:
        try: 
            if len(self.caracteres)>1:
                return self.caracteres[-1]
            return 's'
        except IndentationError:
            print(Pila.PILA_VACIA)
            return 's' 

    def borrar_pila(self) -> None:
        for caracter in self.caracteres:
            del caracter
        del self.caracteres    

    def __str__(self) -> str:
        pila_str: str = '['
        for caracter in self.caracteres:
            pila_str += f'{caracter}, '
        return pila_str+']'
