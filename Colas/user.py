from pago import Pago

class Usuario:
    """
    Representa un usuario genérico.

    Attributes:
        _nombre (str): El nombre del usuario.
        _correo (str): El correo electrónico del usuario.
        _pago (Pago): El objeto de pago asociado al usuario.
    """

    def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
        """
        Inicializa un nuevo usuario.

        Args:
            nombre (str): El nombre del usuario.
            correo (str): El correo electrónico del usuario.
            pago (Pago): El objeto de pago asociado al usuario.
        """
        self._nombre: str = nombre
        self._correo: str = correo
        self._pago: Pago = pago 

class UsuarioPrivilegiado(Usuario):
    """
    Representa un usuario privilegiado que recibe descuentos y promociones adicionales.

    Attributes:
        descuento (float): El porcentaje de descuento aplicado a los pagos.
        promocion (bool): Indica si el usuario tiene una promoción activa.
        _tipo (str): El tipo de usuario.
    """

    def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
        """
        Inicializa un nuevo usuario privilegiado.

        Args:
            nombre (str): El nombre del usuario.
            correo (str): El correo electrónico del usuario.
            pago (Pago): El objeto de pago asociado al usuario.
        """
        super().__init__(nombre, correo, pago)
        self.descuento: float = 0.4
        self.promocion: bool = True
        self._pago.establecer_monto(5000000)
        self._tipo: str = 'PRIVILEGIADO'

    def pagar(self, monto: float) -> bool:
        """
        Realiza un pago con descuento.

        Args:
            monto (float): El monto a pagar.

        Returns:
            bool: True si el pago se realiza correctamente, False en caso contrario.
        """
        return self._pago.pagar(monto*self.descuento)
  
    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de usuario y el tipo de pago.

        Returns:
            str: Una cadena que representa el tipo de usuario y el tipo de pago.
        """
        return self._tipo + ':' + self._pago.obtener_tipo()
  
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del usuario privilegiado.

        Returns:
            str: Una cadena que representa al usuario privilegiado.
        """
        return f"El cliente {self._nombre} con correo {self._correo} tiene un saldo de: {self._pago.obtener_monto()}"

class UsuarioIntermedio(Usuario):
    """
    Representa un usuario intermedio que recibe un descuento moderado.

    Attributes:
        descuento (float): El porcentaje de descuento aplicado a los pagos.
        promocion (bool): Indica si el usuario tiene una promoción activa.
        _tipo (str): El tipo de usuario.
    """

    def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
        """
        Inicializa un nuevo usuario intermedio.

        Args:
            nombre (str): El nombre del usuario.
            correo (str): El correo electrónico del usuario.
            pago (Pago): El objeto de pago asociado al usuario.
        """
        super().__init__(nombre, correo, pago)
        self.descuento: float = 0.2
        self.promocion: bool = False
        self._pago.establecer_monto(3000000)
        self._tipo: str = 'INTERMEDIO'

    def pagar(self, monto: float) -> bool:
        """
        Realiza un pago con descuento.

        Args:
            monto (float): El monto a pagar.

        Returns:
            bool: True si el pago se realiza correctamente, False en caso contrario.
        """
        return self._pago.pagar(monto*self.descuento)
  
    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de usuario y el tipo de pago.

        Returns:
            str: Una cadena que representa el tipo de usuario y el tipo de pago.
        """
        return self._tipo + ':' + self._pago.obtener_tipo()
  
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del usuario intermedio.

        Returns:
            str: Una cadena que representa al usuario intermedio.
        """
        return f"El cliente {self._nombre} con correo {self._correo} tiene un saldo de: {self._pago.obtener_monto()}"
