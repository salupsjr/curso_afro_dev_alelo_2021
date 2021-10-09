#-*-coding:utf8;-*-
#qpy:console
from random import randrange
print("=" * 40)
print("JOGO PAR OU IMPAR".center(40))
print("=" * 40)
ponto = ponto_maquina = 0

while True :
    usuario = int(input("Escolha um número de 0 a 10: "))
    par_impar = input("Escolha PAR ou IMPAR: ")[0]
    maquina  = randrange(11)
    soma = usuario + maquina

    if usuario % 2 == 0:
       resposta = "PAR"
       if par_impar in "Pp":
          ponto += 1
          print(f"Deu {resposta}. Você ganhou essa.")
       else:
          ponto_maquina += 1
          print(f"Deu {resposta}. A máquina ganhou essa.")
    else:
       resposta = "IMPAR"
       if par_impar in "Ii":
          ponto += 1
          print(f"Deu {resposta}. Você ganhou essa.")
       else:
          ponto_maquina += 1
          print(f"Deu {resposta}. A máquina ganhou essa.")
    if ponto == 2 or ponto_maquina  == 2:
       break
   
    soma = 0
if ponto == 2:
   print(f"GAME OVER. Você ganhou o jogo{ponto}: {ponto_maquina } para você.")
else:
   print(f"GAME OVER. A maquina ganhou o jogo por {ponto_maquina}:{ponto} para a máquina.")