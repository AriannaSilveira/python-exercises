#Faça um programa que leia, via input de usuário, um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano: "))
if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse ano é bissexto.")
else:
    print("Esse ano não é bissexto.")