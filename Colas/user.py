from pago import Pago

class Usuario:
  def __init__(self, nombre: str, correo: str, pago:  Pago) -> None:
    self._nombre: str = nombre
    self._correo: str = correo
    self._pago: Pago = pago

class UsuarioPrivilegiado(Usuario):
  def __init__(self, nombre: str, correo: str, monto:  float) -> None:
    super(nombre, correo)
    self.descuento: float = 0.4
    self.promocion: bool = True
    self._monto: float = 3000000

class UsuarioIntermedio(Usuario):
  def __init__(self, nombre: str, correo: str, monto:  float) -> None:
    super(nombre, correo)
    self.descuento: float = 0.2
    self.promocion: bool = False
    self._monto: float = 1500000
