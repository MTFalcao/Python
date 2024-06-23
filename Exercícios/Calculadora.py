import math
def calculadora():
    print("Escolha operação que deseja fazer:\n[1]Operações aritiméticas\n[2]Fatorial\n[3]Raiz Quadrada\n[4]Exponenciação")
    num_esc=int(input("-> "))
    while True:
        if (num_esc==1):
            print("Que tipo de operação aritimética deseja fazer:\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão")
            num_op=int(input("-> "))
            if(num_op==1):
                num1=float(input("Digite o primeiro numero: "))
                num2=float(input("Digite o segundo numero: "))    
                print("A Soma dos seus numeros é: ", num1+num2)
                return
            elif(num_op==2):
                num1=float(input("Digite o primeiro numero: "))
                num2=float(input("Digite o segundo numero: "))  
                if(num1>num2): 
                    print("A subtração dos seus numeros é: ", num1-num2)
                    return
                elif(num2>num1):  
                    print("A subtração dos seus numeros é: ", num2-num1)
                    return
            elif(num_op==3):
                num1=float(input("Digite o primeiro numero: "))
                num2=float(input("Digite o segundo numero: "))  
                print("A Multiplicação dos seus numeros é: ", num1*num2)
                return
            elif(num_op==4):
                num1=float(input("Digite o primeiro numero: "))
                num2=float(input("Digite o segundo numero: "))  
                if (num1>num2):
                    print("A divisão dos seus numeros é: ", num1 /num2)
                    return
                elif (num1<num2):
                    print("A divisão dos seus numeros é: ", num2 / num1)
                    return
        elif (num_esc==2):
            num1=int(input("Digite o numero e veja seu fatorial: "))
            print(math.factorial(num1))
            return
        elif (num_esc==3): 
            num1=int(input("Digite o numero e veja sua Raiz Quadrada: "))
            print(math.sqrt(num1))
            return
        elif(num_esc==4):
            num1=float(input("Digite o numero e veja sua Exponenciação: "))
            print(math.exp(num1))
            return 
                    
calculadora()                 
