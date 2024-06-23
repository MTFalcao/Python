"""Faça um script em Python que calcule o fatorial de um número 𝑛 informado pelo usuário. 
O fatorial de um número é calculado pela multiplicação desse número por todos os seus 
antecessores até chegar ao número 1. """

num=int(input("digite um numero e veja seu fatorial: "))
mult=1

for i in range(1,num+1):
    mult=mult*i
print("o fatorial de",num,"é: ",mult)
