""" Programa em Python que leia o nome de 2 times e o número de gols marcados na partida 
(para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser 
impressa a palavra EMPATE"""

timeA,timeB=str(input("Nome do primeiro time: ")), str(input("Nome do segundo time: "))
gol_timeA,gol_timeB=int(input("Numero de gols do time A marcados na partida: ")),int(input("Numero de gold do time B marcados na partida: "))

if(gol_timeA>gol_timeB):
    print("O vencedor é o time",timeA,"que marcou",gol_timeA,"gols na partida.")
elif(gol_timeA<gol_timeB):
    print("O vencedor é o time",timeB,"que marcou",gol_timeB,"gols na partida.")
else:
    print("A partida terminou com os dois times marcando",gol_timeA,"e acabou sendo um empate.")
