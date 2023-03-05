#Faça um programa que receba, via input de usuário, os valores de duas notas de uma aluna. O programa deve calcular a média e apresentar:
# - A mensagem "Aprovada!", se a média obtida for maior ou igual a 7;
# - A mensagem "Reprovada :(", se a média obtida for menor que 7;
# - A mensagem "Aprovada com distinção :D", se a média obtida for igual a 10.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

if media == 10:
    print("Aprovada com distinção :D")
elif media >= 7:
        print("Aprovada!")
else:
    print("Reprovada :(")