from pago import Pago

class Usuario:
  def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
    self._nombre: str = nombre
    self._correo: str = correo
    self._pago: Pago = pago 

class UsuarioPrivilegiado(Usuario):
  def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
    super().__init__(nombre, correo, pago)
    self.descuento: float = 0.4
    self.promocion: bool = True
    self._pago.establecer_monto(5000000)
    self._tipo: str = 'PRIVILEGIADO'

  def pagar(self, monto: float) -> bool:
    return self._pago.pagar(monto*self.descuento)
  
  def obtener_tipo(self) -> str:
    return self._tipo+':'+self._pago.obtener_tipo()

class UsuarioIntermedio(Usuario):
  def __init__(self, nombre: str, correo: str, pago: Pago) -> None:
    super().__init__(nombre, correo, pago)
    self.descuento: float = 0.2
    self.promocion: bool = False
    self._pago.establecer_monto(3000000)
    self._tipo: str = 'INTERMEDIO'

  def pagar(self, monto: float) -> bool:
    return self._pago.pagar(monto*self.descuento)
  
  def obtener_tipo(self) -> str:
    return self._tipo+':'+self._pago.obtener_tipo()