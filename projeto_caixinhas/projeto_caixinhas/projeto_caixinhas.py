def caixinha():
    valores = {'viagem':0, 'carro':0}
    while True:

        print("\nO que você deseja fazer?")
        print("1 - Adicionar dinheiro")
        print("2 - Retirar dinheiro")
        print("3 - Verificar saldo")
        print("4 - Sair")
        atividade = input("Atividade: ")
        if atividade == "4":
            break
        elif atividade == "3":
            saldo(valores)
        elif atividade == "1":
            caixinha = input("Caixinha: ")
            while caixinha not in valores:
                print("Digite um nome válido para a caixinha")
                chaves_caixinha=[]
                for chaves in valores.keys():
                    chaves_caixinha.append(chaves)
                print(chaves_caixinha)
                caixinha = input("Caixinha: ")
            valor = int(input("Valor: "))
            adicionar(caixinha, valores, valor)
        elif atividade == "2":
            caixinha = input("Caixinha: ")
            while caixinha not in valores:
                print("Digite um nome válido para a caixinha")
                chaves_caixinha=[]
                for chaves in valores.keys():
                    chaves_caixinha.append(chaves)
                print(chaves_caixinha)
                caixinha = input("Caixinha: ")
            valor = int(input("Valor: "))
            retirar(caixinha, valores, valor)
        else:
            print("Digite uma opção válida")
    return valores

def retirar(caixinha,valores, valor):
    if valor > valores[caixinha]:
        return print("Não é possivel retirar esse valor por falta de saldo")
    valores[caixinha]=valores[caixinha]-valor
    return valores

def adicionar(caixinha,valores, valor):
    valores[caixinha]=valores[caixinha]+valor
    return valores

def saldo(valores):
    print(valores)

caixinha()