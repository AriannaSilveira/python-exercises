#Faça uma função que receba parâmetros variáveis. Faça algumas chamadas dessa função passando valores inteiros e, de acordo com a quantidade de parâmetros recebidos, calcule a média.

def media_params(*valores):
    soma = 0
    for valor in valores:
        soma += valor
    if len(valores) != 0:
        media = soma/len(valores)
    else:
        media = 0
    return media

print(media_params(1,2))
print(media_params(1))
print(media_params(1,2,3))
print(media_params(1,2,3,4,5,87,3))
print(media_params())