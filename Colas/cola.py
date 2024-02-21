class Cola:
    COLA_VACIA: str = "La cola se encuentra vacía"

    def __init__(self) -> None:
        self.datos: tuple[bool, int, str] = []
        
    def queue(self, X: tuple[bool, int, str]) -> None:
         self.datos.append(X)

    def dequeue(self) -> str | None:
        try:
            return self.datos.pop(0)
        except IndexError:
            print(Cola.COLA_VACIA)

    def esta_vacia(self) -> bool:
        return self.datos == []

    def tam(self) -> int :
        return len(self.datos)

    def borrar_pila(self) -> None:
        for dato in self.datos:
            del dato
        del self.datos    

    def __str__(self) -> str:
        pila_str: str = '['
        for dato in self.datos:
            pila_str += f'{dato}, '
        return pila_str+']'
