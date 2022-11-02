from Cuadrado import Cuadarado

num = int(input('Ingrese cuanto mide el lado del cuadrado'))
c1 = Cuadarado(num,'azul')
print(f'El area del cuadrado es: {c1.area()}')
print(c1.__str__())