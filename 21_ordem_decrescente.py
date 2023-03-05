#Faça um programa que leia via linha de comando tês números e mostre-os em ordem decrescente.

import sys

lista = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

lista.sort(reverse=True)

print("Os números em ordem decrescente são dados por:", lista)