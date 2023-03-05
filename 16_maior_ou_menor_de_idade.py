#Faça um programa que peça uma idade via input de usuário e mostre na tela uma mensagem informando se essa pessoa é maior ou menor de idade.

idade = input("Digite sua idade: ")

if int(idade) >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")