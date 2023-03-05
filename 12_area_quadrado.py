#Faça um programa que peça via linha de comando o valor do lado de um quadrado e faça o cálculo da área.

import sys;

lado = sys.argv[1];

area = float(lado)*float(lado);

print("A área desse quadrado é:", area)