#Gabriel para o Marcao: <Calculadora em Python> 
numero1 = 0
numero2 = 0
operacao = 0
a = []

#Funcao em que a entrada eh em passos
def Alpha():

    #Condicao do operador
    numero1 = float(input("Digite o primeiro numero: "))##variavel decimal numero 1
    print(" ")
    operacao = input("Digite a operacao: ")##operacao que sera realizada
    print(" ")
    numero2 = float(input("Digite o numero 2: "))#variavel decimal numero 2
    print(" ")
    
    print(str(numero1) + " " + str(operacao) + " " + str(numero2) + " " + " = " + str(OP(numero1, numero2, operacao))) #Ainda esta na funcao, printa o resultado
    
    print(" ")
    
    Beta(OP(numero1, numero2, operacao)) #Chama a funcao para salvar os dados, para visualizacao
    
    print(" ")

#Funcao em que a entrada eh uma operacao completa
def Gamma():
     
        d = input("Comece aqui a operacao completa: ")
        print(" ")
        dados = d.split(" ")
        
        numero1 = float(dados[0])
        
        numero2 = float(dados[2])
        
        operacao = str(dados[1])
        
        print(str(numero1) + " " + str(operacao) + " " + str(numero2) + " " + " = " + str(OP(numero1, numero2, operacao)))
        
        print(" ")
         
        Beta(OP(numero1, numero2, operacao)) #Chama a funcao para salvar os dados, para visualizacao
        
        print(" ")
        
#Funcao que seleciona o operador, essencial para a calculadora
def OP(num1, num2, opera):
    if opera == "+":
        return num1 + num2
    elif opera == "-":
        return num1 - num2
    elif opera == "/":
        return num1 / num2
    elif opera == "*":
        return num1 * num2
    else:
        return "Operacao invalida"



#Funcao que salva o numero para visualizacao
def Beta(resultado):
    print("1. M+    2. M-   3. M_Limpar     4. None")
    
    print(" ")

    option = str(input())

    if option == "1":
        a.append(resultado)
    
        print("M+" + "=" + str(a))
    elif option == "2":
    
        if a != 0:
            n = int(a.count()) #conta quantos elementos tem na lista.
            a.remove(n)#Remove o ultimo elemento da lista
            
            print("M+" + "=" + str(a))

        else :
            Alpha()
            
            print("M+" + "=" + str(a))
    
    elif option == "3":
        a.clear()
        
        print("M+" + "=" + str(a))
    
    elif option == "4":
        Alpha()
        

    else:
        print("Operacao Invalida")
        Beta()

def Total():
    print("1. Fazer numero por numero?")

    print(" ")

    print("2. Colocar a Operacao?")

    print(" ")

    k = input("Escolha uma opcao: ")

    print(" ")

    if k == "1":
        while True:
        ##Esse looping serve para repetir o processo diversas vezes
            Alpha()

    elif k == "2": 
        while True:
        ##Esse looping serve para repetir o processo diversas vezes
            print("Coloque a equacao, separando por espaço os numeros e o operador, como no exemplo abaixo")
            print(" ")
            print("ex: Num1 + Num2(Enter)")
            print(" ")
            Gamma() #Chama a funcao definida
    else: 
        print("Operacao Invalida")
        Total()


Total()
