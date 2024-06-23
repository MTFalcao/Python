"""Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, 
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se 
saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão 
escrever a mensagem 'Saldo Negativo'"""

conta=int(input("Digite o numero da sua conta: "))
saldo,debito,credito= float(input("Digite o saldo da sua conta: ")), float(input("Digite o debito da sua conta: ")),float(input("Digite o credito da sua conta: "))

saldo_atual=(saldo - debito + credito)

print("Conta do usuario: ",conta)
print("Saldo atual: ",saldo_atual)
if (saldo_atual>=0):
    print("Seu saldo é positivo")
else:
    print("Seu saldo é negativo")
