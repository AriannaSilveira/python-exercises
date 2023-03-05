#Faça um programa que leia um número via input de usuário e exiba o dia correspondente da semana (1 - Domingo, 2 - Segunda, etc). Para valores negativos ou maiores que 7, exibir a mensagem "Valor inválido!".

dia = int(input("Digite um número de 1 a 7 para descobrir o dia correspondente da semana: "))

if dia == 1:
    print("Domingo.")
elif dia == 2:
    print("Segunda-feira.")
elif dia == 3:
    print("Terça-feira.")
elif dia == 4:
    print("Quarta-feira.")
elif dia == 5:
    print("Quinta-feira.")
elif dia == 6:
    print("Sexta-feira.")
elif dia == 7:
    print("Sábado.")
else:
    print("Valor inválido!")