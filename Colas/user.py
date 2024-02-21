
class Usuario:
  def __init__(self, nombre: str, correo: str) -> None:
    self._nombre: str = nombre
    self._correo: str = correo

class UsuarioPrivilegiado(Usuario):
  def __init__(self, nombre: str, correo: str) -> None:
    super(nombre, correo)
    self.descuento: float = 0.4
    self.promocion: bool = True

class UsuarioIntermedio(Usuario):
  def __init__(self, nombre: str, correo: str) -> None:
    super(nombre, correo)
    self.descuento: float = 0.2
    self.promocion: bool = False
