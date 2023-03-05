#Faça uma função que recebe 4 notas em valor decimal (entre 0 e 10). Caso a nota seja menor que 5, retorna "Reprovada". Caso a nota seja entre 5 e 7, retorna "Está na média". Caso a nota seja maior que 7, retorna "Aprovada".

def media_notas(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4)/4
    if media < 5:
        return "Reprovada."
    elif media > 5 and media < 7:
        return "Está na média."
    else:
        return "Aprovada!"

print("SITUAÇÃO ALUNA 1:", media_notas(5.5, 1, 2, 1.2))
print("SITUAÇÃO ALUNA 2:", media_notas(5.5, 6, 6.5, 6))
print("SITUAÇÃO ALUNA 3:", media_notas(9.5, 10, 7.5, 7))