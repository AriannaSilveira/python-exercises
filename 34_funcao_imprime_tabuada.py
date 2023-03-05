#Faça uma função que imprime a tabuada de 2 ao 9.

def imprime_tabuada():
    for i in range(2, 10):
        print("----------------------------------------------------------------")
        print("                      TABUADA DO " + str(i))
        print("----------------------------------------------------------------")
        for j in range(10):
            result = i * j
            print(str(i) + " x " + str(j) + " = " + str(result))

imprime_tabuada()