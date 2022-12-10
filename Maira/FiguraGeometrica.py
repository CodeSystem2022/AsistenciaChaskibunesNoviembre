class FiguraGeometrica:
  def __init__(self, ancho, alto):
    if self._validar_valores(ancho):
      self.ancho = ancho
    else:
      self._ancho = 0
      print(f'Valor erroneo de ancho: {ancho}')
    if self._validar_valores(alto):
      self._alto = alto
    else:
      self._alto = 0
      print(f'Valor erroneo de alto:{alto}')
      
@property
def ancho(self):
  return self._ancho

@ancho.setter
def ancho(self, ancho):
  if self._validar_valores(ancho):
    
def __str__(self):
  return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
