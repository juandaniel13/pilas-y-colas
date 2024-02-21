
class Pago:
  def __init__(self) -> None:
    self._monto: float = 0
  
  def establecer_monto(self, monto: float) -> None:
    self._monto = monto

  def obtener_monto(self) -> float:
    return self._monto

class PagoEfectivo(Pago):
  def __init__(self) -> None:
    super()
    self._descuento: float = 0.02

  def pagar(self, monto_a_pagar: float) -> float:
    if (monto_a_pagar*self._descuento) > self._monto:
      return 0

    self._monto-=(monto_a_pagar*self._descuento)
    return monto_a_pagar

class PagoDigital(Pago):
  def __init__(self) -> None:
    super()
    self._descuento: float = 0.02

  def pagar(self, monto_a_pagar: float) -> float:
    if (monto_a_pagar*self._descuento) > self._monto:
      return 0

    self._monto-=(monto_a_pagar*self._descuento)
    return monto_a_pagar