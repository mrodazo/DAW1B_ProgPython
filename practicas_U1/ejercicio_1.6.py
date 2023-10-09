"""Escribe un programa que pida el importe final de un artículo y calcule
 e imprima por pantalla el IVA que se ha pagado y el importe sin IVA
(suponiendo que se ha aplicado un tipo de IVA del 10%)."""

impIVA = float(input('Indique el importe final:\n'))
impSIN = impIVA / (1.1) #Ya que el IVA es del 10%
print('El IVA aplicado es del 10%, así que el precio sin IVA es de', '{: .2f}'.format(impSIN), '€')