"""Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo na linguagem 
Python que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não."""

nome=str(input("Digite seu nome: "))
idade=int(input("Digite sua idade e descubra se pode doar sangue: "))

if(idade>=18 and idade<=67):
    print(nome,"você está elegivel para doar sangue.")
elif(idade<18):
    print(nome,"você é menor de idade, infelizmente não pode doar sangue.")
elif(idade>67):
    print(nome,"infelizmente você passou da idade de doar sangue, que é até 67 anos, você não pode doar sangue.")
