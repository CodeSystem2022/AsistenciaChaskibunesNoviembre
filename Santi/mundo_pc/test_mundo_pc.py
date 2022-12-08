from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

monitor1 = Monitor('HP', '15 Pulgadas')
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

monitor2 = Monitor('Acer', '27 Pulgadas')
teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

monitor3 = Monitor('Samsung', '15 Pulgadas')
teclado3 = Teclado('Samsung', 'USB')
raton3 = Raton('Samsung', 'USB')
computadora3 = Computadora('Samsung', monitor3, teclado3, raton3)

monitor4 = Monitor('Apple', '27 Pulgadas')
teclado4 = Teclado('Apple', 'Bluetooth')
raton4 = Raton('Apple', 'Bluetooth')
computadora4 = Computadora('Apple', monitor4, teclado4, raton4)

monitor5 = Monitor('Gamer', '15 Pulgadas')
teclado5 = Teclado('Gamer', 'USB')
raton5 = Raton('Gamer', 'USB')
computadora5 = Computadora('Gamer', monitor5, teclado5, raton5)

computadora6 = Computadora('Acer', monitor2, teclado3, raton5)
computadora7 = Computadora('Gamer', monitor4, teclado2, raton1)

computadoras1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora5, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)
