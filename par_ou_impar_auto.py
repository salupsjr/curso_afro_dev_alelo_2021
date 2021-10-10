from random import randrange, choice
from time import sleep

print("=*=" * 15)
print("Bem vindo ao jogo de PAR ou IMPAR automático.".center(15))
print("=*=" * 15)
s = sleep(3)
quantidade_rodadas = int(input("Quantas rodadas você quer que ocorra? Resposta: "))

if quantidade_rodadas % 2 == 0:
    print("=*=" * 15)
    print("ATENÇÃO!!!".center(45))
    print("=*=" * 15)
    print("Você escolheu um número PAR para a quantidade \nde rodadas e isso pode acarretar em um EMPATE.".center(45))
sleep(3)
print("\nJOGO EM ANDAMENTO AGUARDE...")
sleep(3)
print("\nJOGO FINALIZADO!")
par_impar = ["PAR", "IMPAR"]

escolha_pc1 = choice(par_impar)
pontos_pc1 = pontos_pc2 = 0


for rodada in range(quantidade_rodadas):
        pc1 = randrange(10)
        pc2 = randrange(10)
        soma = pc1 + pc2
        if soma % 2 == 0: 
            if "PAR" in escolha_pc1:
                pontos_pc1 += 1
            else:
                pontos_pc2 += 1
        else: 
            if "IMPAR" in escolha_pc1:
                pontos_pc1 += 1
            else:
                pontos_pc2 += 1
                
if pontos_pc1 > pontos_pc2:
    print(f"\nO vencedor é o COMPUTADOR 1 que venceu {pontos_pc1} partidas. O placar foi de {pontos_pc1} x {pontos_pc2}.")
elif pontos_pc1 < pontos_pc2:    
    print(f"\nO vencedor é o COMPUTADOR 2 que venceu {pontos_pc2} partidas. O placar foi de {pontos_pc2} x {pontos_pc1}.")
else: 
    print(f"\nHouve um empate. O placar foi de {pontos_pc1} x {pontos_pc2}.")