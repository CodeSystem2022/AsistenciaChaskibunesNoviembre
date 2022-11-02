import imp
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadarado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self,color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self) -> str:
        return f'Cuadrado: \n{FiguraGeometrica.__str__(self)}\n{Color.__str__(self)}'