#Faça um programa que receba dois números inteiros via linha de comando e gere os números inteiros que estão no intervalo compreendido por eles.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

for i in range(num1 + 1, num2):
    print(i)