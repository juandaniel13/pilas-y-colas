
class Pago:
  def __init__(self) -> None:
    self._monto: float = 0
  
  def establecer_monto(self, monto: float) -> None:
    self._monto = monto

  def obtener_monto(self) -> float:
    return self._monto

class PagoEfectivo(Pago):
  def __init__(self) -> None:
    super().__init__()
    self._descuento: float = 0.02

  def pagar(self, monto_a_pagar: float) -> bool:
    if (monto_a_pagar*self._descuento) > self._monto:
      return False

    self._monto-=(monto_a_pagar*self._descuento)
    return True
  
  def obtener_tipo(self) -> str:
    return 'EFECTIVO'

class PagoDigital(Pago):
  def __init__(self) -> None:
    super().__init__()
    self._descuento: float = 0.02

  def pagar(self, monto_a_pagar: float) -> bool:
    if (monto_a_pagar*self._descuento) > self._monto:
      return False

    self._monto-=(monto_a_pagar*self._descuento)
    return True

  def obtener_tipo(self) -> str:
    return 'DIGITAL'
