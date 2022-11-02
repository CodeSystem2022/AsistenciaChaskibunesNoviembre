from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        #super().__init__(ancho, alto)
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.alto

    def __str__(self) -> str:
        return f'Rectangulo: \n{FiguraGeometrica.__str__(self)}\n{Color.__str__(self)}'