#Faça uma função que recebe 5 números e imprime a soma e a média dos números.

def soma_e_media(num1, num2, num3, num4, num5):
    soma = num1 + num2 + num3 + num4 + num5
    media = soma/5
    print ("Soma:", soma)
    print("Média:", media)

soma_e_media(1,2,3,4,4)