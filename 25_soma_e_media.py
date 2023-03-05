#Usando estruturas de repetição, faça um programa que leia 5 números via input e exiba a soma e a média dos números.

numeros = []
for _ in range (5):
    numeros.append(float(input("Digite um número: ")))

soma = 0
for i in range(5):
    soma += numeros[i]

media = soma/5

print("Soma:", soma)
print("Média:", media)