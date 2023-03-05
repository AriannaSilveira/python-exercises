#Faça um programa que peça via linha de comando as 4 notas bimestrais e mostre a média.

import sys;

nota1 = sys.argv[1];
nota2 = sys.argv[2];
nota3 = sys.argv[3];
nota4 = sys.argv[4];

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4;

print("A média é: ", media)