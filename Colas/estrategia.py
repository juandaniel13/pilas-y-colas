from user import Usuario

class Estrategia:
    """
    Define la interfaz para realizar un pago por un usuario.
    """

    def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> bool:
        """
        Realiza un pago por un usuario.

        Args:
            usuario (Usuario): El usuario para el que se realiza el pago.
            monto (float): El monto del pago.

        Returns:
            bool: True si el pago se realiza correctamente, False en caso contrario.
        """
        pass

class EstrategiaPagoEfectivoPrivilegiado(Estrategia):
    """
    Estrategia de pago efectivo para usuarios privilegiados.
    """

    def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
        """
        Realiza un pago en efectivo para un usuario privilegiado.

        Args:
            usuario (Usuario): El usuario para el que se realiza el pago.
            monto (float): El monto del pago.

        Returns:
            tuple[bool, int]: Una tupla que indica si el pago fue exitoso y el tipo de pago.
        """
        pago_exitoso = usuario.pagar(monto)
        if not pago_exitoso:
            return (False, 0)
        return (True, 2)

class EstrategiaPagoDigitalPrivilegiado(Estrategia):
    """
    Estrategia de pago digital para usuarios privilegiados.
    """

    def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
        """
        Realiza un pago digital para un usuario privilegiado.

        Args:
            usuario (Usuario): El usuario para el que se realiza el pago.
            monto (float): El monto del pago.

        Returns:
            tuple[bool, int]: Una tupla que indica si el pago fue exitoso y el tipo de pago.
        """
        pago_exitoso = usuario.pagar(monto)
        if not pago_exitoso:
            return (False, 0)
        return (True, 2)

class EstrategiaPagoEfectivoIntermedio(Estrategia):
    """
    Estrategia de pago efectivo para usuarios intermedios.
    """

    def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
        """
        Realiza un pago en efectivo para un usuario intermedio.

        Args:
            usuario (Usuario): El usuario para el que se realiza el pago.
            monto (float): El monto del pago.

        Returns:
            tuple[bool, int]: Una tupla que indica si el pago fue exitoso y el tipo de pago.
        """
        pago_exitoso = usuario.pagar(monto)
        if not pago_exitoso:
            return (False, 0)
        return (True, 1)

class EstrategiaPagoDigitalIntermedio(Estrategia):
    """
    Estrategia de pago digital para usuarios intermedios.
    """

    def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
        """
        Realiza un pago digital para un usuario intermedio.

        Args:
            usuario (Usuario): El usuario para el que se realiza el pago.
            monto (float): El monto del pago.

        Returns:
            tuple[bool, int]: Una tupla que indica si el pago fue exitoso y el tipo de pago.
        """
        pago_exitoso = usuario.pagar(monto)
        if not pago_exitoso:
            return (False, 0)
        return (True, 1)

ESTRATEGIA_PAGO_DIGITAL_INTERMEDIO = EstrategiaPagoDigitalIntermedio()
ESTRATEGIA_PAGO_EFECTIVO_INTERMEDIO = EstrategiaPagoEfectivoIntermedio()
ESTRATEGIA_PAGO_DIGITAL_PRIVILEGIADO = EstrategiaPagoDigitalPrivilegiado()
ESTRATEGIA_PAGO_EFECTIVO_PRIVILEGIADO = EstrategiaPagoEfectivoPrivilegiado()

class ContextoEstrategia:
    """
    Define el contexto para utilizar una estrategia de pago específica.
    """

    def __init__(self):
        """
        Inicializa un nuevo contexto de estrategia.
        """
        self._estrategia_concreta: Estrategia | None = None

    def establecer_estrategia(self, usuario: Usuario) -> None:
        """
        Establece la estrategia de pago concreta basada en el tipo de usuario.

        Args:
            usuario (Usuario): El usuario para el que se establece la estrategia.
        """
        if usuario.obtener_tipo() == 'PRIVILEGIADO:EFECTIVO':
            self._estrategia_concreta = ESTRATEGIA_PAGO_EFECTIVO_PRIVILEGIADO
        elif usuario.obtener_tipo() == 'PRIVILEGIADO:DIGITAL':
            self._estrategia_concreta = ESTRATEGIA_PAGO_DIGITAL_PRIVILEGIADO
        elif usuario.obtener_tipo() == 'INTERMEDIO:EFECTIVO':
            self._estrategia_concreta = ESTRATEGIA_PAGO_EFECTIVO_INTERMEDIO
        elif usuario.obtener_tipo() == 'INTERMEDIO:DIGITAL':
            self._estrategia_concreta = ESTRATEGIA_PAGO_DIGITAL_INTERMEDIO

    def definir_pago(self, monto: float, usuario: Usuario) -> tuple[bool, int]:
        """
        Define el pago utilizando la estrategia de pago concreta.

        Args:
            monto (float): El monto del pago.
            usuario (Usuario): El usuario para el que se realiza el pago.

        Returns:
            tuple[bool, int]: Una tupla que indica si el pago fue exitoso y el tipo de pago.
        """
        return self._estrategia_concreta.realizar_pago_por_usuario(usuario, monto)
