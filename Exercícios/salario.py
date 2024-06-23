""" Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 
1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário 
total. """

sal=float(input("Digite seu salario: "))
ven=float(input("Digite ganho em vendas: "))

com=ven*0.03

if(ven<=1500):
    sal_F=com+sal
    print("Seu salario final com 3% das vendas, ficou no valor de: ",sal_F)
else:
    com2=((ven-1500)*0.05 + (1500*0.03))
    sal_F2=com2+sal
    print("Seu salario final com 5% das vendas, ficou no valor de: ",sal_F2)
