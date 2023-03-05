#Usando loops, fazer um programa que mostra a tabuada do dois até o nove.

for i in range(2, 10):
    print("----------------------------------------------------------------")
    print("                      TABUADA DO " + str(i))
    print("----------------------------------------------------------------")
    for j in range(10):
        result = i * j
        print(str(i) + " x " + str(j) + " = " + str(result))