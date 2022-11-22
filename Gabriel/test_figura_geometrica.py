from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print("Creación de objetos clase Cuadrado".center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())
print(cuadrado1)

print("Creación de objetos clase Rectángulo".center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'Rojo')
rectangulo1.ancho = 8
# print(rectangulo1.alto)
# print(rectangulo1.ancho)
# print(rectangulo1.color)
print(f'Cálculo del área del cuadrado: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica(x, y)  ---> No se puede instancias, es abstracta
print(Cuadrado.mro())
