#Usando estruturas de repetição, faça um programa que leia 5 números via input e exiba qual é o maior número.

numeros = []
for _ in range (5):
    numeros.append(float(input("Digite um número: ")))
    
maior = numeros[0]
for i in range(1,5):
    if maior < numeros[i]:
        maior = numeros[i]
print("O maior é:", maior)