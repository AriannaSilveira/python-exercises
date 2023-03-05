#Faça uma função que receba um argumento inteiro. A função retorno P se o valor for positivo e N se seu valor for zero ou negativo.

def positivo_ou_negativo(valor):
    if valor > 0:
        return "P"
    else:
        return "N"

print(positivo_ou_negativo(1))
print(positivo_ou_negativo(0))
print(positivo_ou_negativo(-9))