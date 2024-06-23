"""Escreva um algoritmo em Python que leia o número de litros vendidos e o tipo de 
combustível (codificado da seguinte forma: 1 - álcool, 2 - gasolina), calcule e imprima o 
valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o 
preço do litro do álcool é R$ 2,90. Os cálculos finais são definidos de acordo com a tabela 
abaixo: Alcool - Até 20 litros, desconto de 3% por litro. / acima de 20 litros, desconto de 5% por litro.
Gasolina - Até 20 litros, desconto de 4% por litro. / acima de 20 litros, desconto de 6% por litro. """

num=int(input("Digite 1 se deseja comprar alcool ou se deseja comprar gasolina digite 2:  "))

if (num==1):
    qtd_alc=float(input("Digite a quantidade de litros de alcool que deseja comprar: "))
    if(qtd_alc<=0):
        print("Quantidade invalida")
    elif (qtd_alc<=20):
        alc=3.30-(3.3*0.03)
        valf_alc= qtd_alc*alc
        print(f"O valor do alcool saiu a: {valf_alc:.2f} reais")
    elif(qtd_alc>20):
        alc=3.30-(3.3*0.05)
        valf_alc= qtd_alc*alc
        print(f"O valor do alcool saiu a: {valf_alc:.2f} reais")
elif(num==2):
    qtd_gaso=float(input("Digite a quantidade de litros de gasolina que deseja comprar: "))
    if(qtd_gaso<=0):
        print("Quantidade invalida")
    elif (qtd_gaso<=20):
        gaso=2.90-(2.9*0.04)
        valf_gaso= qtd_gaso*gaso
        print(f"O valor do alcool saiu a: {valf_gaso:.2f} reais")
    elif(qtd_gaso>20):
        gaso=2.90-(2.9*0.06)
        valf_gaso= qtd_gaso*gaso
        print(f"O valor do alcool saiu a: {valf_gaso:.2f} reais")
