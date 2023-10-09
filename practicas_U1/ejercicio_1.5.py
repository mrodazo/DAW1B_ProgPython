"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA
 a aplicar y calcule e imprima por pantalla el precio final del artículo."""

importe = float(input('Indique el importe del artículo sin IVA:\n'))
iva = float(input('% de IVA:\n'))
impIVA = importe + importe * (iva/100) # impIVA = importe * (1 + iva/100)
print(impIVA)