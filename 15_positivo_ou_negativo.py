#Faça um programa que peça um valor via input de usuário e mostre na tela se o valor é positivo ou negativo.

valor = input("Digite um número: ")

if float(valor) > 0:
    print("O valor dado é positivo.")
elif float(valor) < 0:
    print("O valor dado é negativo.")
else:
    print("O valor dado é nulo.")