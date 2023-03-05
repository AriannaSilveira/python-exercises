#Faça um programa que leia três números via input e mostre o maior deles.

num1 = input("Digite um número: ")
num2 = input("Digite outro número:")
num3 = input("Só mais umzinho, por favor: ")

if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)