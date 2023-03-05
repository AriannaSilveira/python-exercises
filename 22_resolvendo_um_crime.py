#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime:
# - "Falou com a vítima no dia do crime?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia dinheiro para a vítima:"
# - "Já trabalhou com a vítima?"
#Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita.". Entre 3 e 4, como "Cúmplice.". E 5 como "Assassina.". Caso contrário, ela deve ser classificada como "Inocente.".

print("----------------------------------------------------------------")
print("                      SISTEMA JULGADOR")
print("----------------------------------------------------------------")
print("")
print("Responda as perguntas a seguir com honestidade:")
print("")

resposta1 = input("1. Falou com a vítima no dia do crime? (y/n) ")
resposta2 = input("2. Esteve no local do crime? (y/n) ")
resposta3 = input("3. Mora perto da vítima? (y/n) ")
resposta4 = input("4. Devia dinheiro para a vítima? (y/n) ")
resposta5 = input("5. Já trabalhou com a vítima? (y/n) ")

respostas = [resposta1, resposta2, resposta3, resposta4, resposta5]
verdade = "y"
frequencia = respostas.count(verdade)

print("")
if frequencia == 2:
    print("Você foi classificada como Pessoa Suspeita.")
elif 3 >= frequencia >= 4:
    print("Você foi classificada como Pessoa Cúmplice.")
elif frequencia == 5:
    print("Você foi classificada como Pessoa Assassina.")
else:
    print("Você foi classificada como Pessoa Inocente.")