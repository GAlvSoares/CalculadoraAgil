# Interface Simples

print("Escolha uma das opções abaixo: ")
print("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação")



#Input 
esc = int(input("Opção Escolhida: "))

a = int(input("Primeiro Numero: "))
b = int(input("Segundo Numero: "))

#Definindo Opções
#Opção 1
def op1():
    print("A soma é " , (a+b))

#Opção 2
def op2():
    print("A subtração é " , (a-b))

#Opção 3
def op3():
    print("A divisão é " , (a/b))

#Opção 4
def op4():
    print("A multiplicação é " , (a*b))

#Switch Case
if esc == 1:
    op1()
elif esc == 2:
    op2()
elif esc == 3:
    op3()
elif esc == 4:
    op4()



