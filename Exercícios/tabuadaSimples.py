"""Crie um algoritmo em Python que, dado um número informado pelo usuário, imprima a 
tabuada dele de 1 a 10. Use o formato de apresentação."""

num=int(input("digite um numero e veja sua tabuada: "))

for mult in range(10):
    print(f"{num}x{mult+1}={num*(mult+1)}")
