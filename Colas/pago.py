class Pago:
    """
    Representa un pago genérico.

    Attributes:
        _monto (float): El monto del pago.
    """

    def __init__(self) -> None:
        """
        Inicializa un nuevo pago con un monto inicial de 0.
        """
        self._monto: float = 0
  
    def establecer_monto(self, monto: float) -> None:
        """
        Establece el monto del pago.

        Args:
            monto (float): El monto a establecer.
        """
        self._monto = monto

    def obtener_monto(self) -> float:
        """
        Obtiene el monto del pago.

        Returns:
            float: El monto del pago.
        """
        return self._monto

class PagoEfectivo(Pago):
    """
    Representa un pago en efectivo.

    Attributes:
        _descuento (float): El porcentaje de descuento aplicado al pagar en efectivo.
    """

    def __init__(self) -> None:
        """
        Inicializa un nuevo pago en efectivo con un descuento del 2%.
        """
        super().__init__()
        self._descuento: float = 0.02

    def pagar(self, monto_a_pagar: float) -> bool:
        """
        Realiza un pago en efectivo.

        Args:
            monto_a_pagar (float): El monto a pagar.

        Returns:
            bool: True si el pago se realiza correctamente, False en caso contrario.
        """
        if (monto_a_pagar*self._descuento) > self._monto:
            return False

        self._monto -= (monto_a_pagar * self._descuento)
        return True
  
    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de pago.

        Returns:
            str: El tipo de pago ('EFECTIVO').
        """
        return 'EFECTIVO'

class PagoDigital(Pago):
    """
    Representa un pago digital.

    Attributes:
        _descuento (float): El porcentaje de descuento aplicado al pagar de forma digital.
    """

    def __init__(self) -> None:
        """
        Inicializa un nuevo pago digital con un descuento del 2%.
        """
        super().__init__()
        self._descuento: float = 0.02

    def pagar(self, monto_a_pagar: float) -> bool:
        """
        Realiza un pago digital.

        Args:
            monto_a_pagar (float): El monto a pagar.

        Returns:
            bool: True si el pago se realiza correctamente, False en caso contrario.
        """
        if (monto_a_pagar*self._descuento) > self._monto:
            return False

        self._monto -= (monto_a_pagar * self._descuento)
        return True

    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de pago.

        Returns:
            str: El tipo de pago ('DIGITAL').
        """
        return 'DIGITAL'
