
from user import Usuario

class Estrategia:
  def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> bool:
    pass

class EstrategiaPagoEfectivoPrivilegiado(Estrategia):
  def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
    pago_exitoso = usuario.pagar(monto)
    if not pago_exitoso:
      return (False, 0)
    
    return (True, 2)

class EstrategiaPagoDigitalPrivilegiado(Estrategia):
  def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
    pago_exitoso = usuario.pagar(monto)
    if not pago_exitoso:
      return (False, 0)
    
    return (True, 2)

class EstrategiaPagoEfectivoIntermedio(Estrategia):
  def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
    pago_exitoso = usuario.pagar(monto)
    if not pago_exitoso:
      return (False, 0)
    
    return (True, 1)

class EstrategiaPagoDigitalIntermedio(Estrategia):
  def realizar_pago_por_usuario(self, usuario: Usuario, monto: float) -> tuple[bool, int]:
    pago_exitoso = usuario.pagar(monto)
    if not pago_exitoso:
      return (False, 0)
    
    return (True, 1)

ESTRATEGIA_PAGO_DIGITAL_INTERMEDIO = EstrategiaPagoDigitalIntermedio()
ESTRATEGIA_PAGO_EFECTIVO_INTERMEDIO = EstrategiaPagoEfectivoIntermedio()
ESTRATEGIA_PAGO_DIGITAL_PRIVILEGIADO = EstrategiaPagoDigitalPrivilegiado()
ESTRATEGIA_PAGO_EFECTIVO_PRIVILEGIADO = EstrategiaPagoEfectivoPrivilegiado()

class ContextoEstrategia:
  def __init__(self):
    self._estrategia_concreta: Estrategia | None = None

  def establecer_estrategia(self, usuario: Usuario) -> None:
    if usuario.obtener_tipo() == 'PRIVILEGIADO:EFECTIVO':
      self._estrategia_concreta = ESTRATEGIA_PAGO_EFECTIVO_PRIVILEGIADO
    elif usuario.obtener_tipo() == 'PRIVILEGIADO:DIGITAL':
      self._estrategia_concreta = ESTRATEGIA_PAGO_DIGITAL_PRIVILEGIADO
    elif usuario.obtener_tipo() == 'INTERMEDIO:EFECTIVO':
      self._estrategia_concreta = ESTRATEGIA_PAGO_EFECTIVO_INTERMEDIO
    elif usuario.obtener_tipo() == 'INTERMEDIO:DIGITAL':
      self._estrategia_concreta = ESTRATEGIA_PAGO_DIGITAL_INTERMEDIO

  def definir_pago(self, monto: float, usuario: Usuario) -> tuple[bool, int]:
    return self._estrategia_concreta.realizar_pago_por_usuario(usuario, monto)