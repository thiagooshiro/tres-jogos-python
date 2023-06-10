# Desafio 2:

# Vamos construir um jogo de "Pedra, papel, tesoura"!
# Um jogador humano irá disputar contra a máquina.
# Esse jogador deverá escolher entre "pedra", "papel" ou "tesoura" como manobras válidas.
# Caso a escolha do jogador seja inválida, o jogo em si não deve acontecer
# e uma mensagem de erro "Jogada inválida" deve ser exibida.
# 
# O Computador deve escolher entre "pedra", "papel" ou "tesoura" de forma aleatória.
# E só relembrando: papel perde tesoura, tesoura vence papel, papel vence pedra.
# Se a jogada for válida o programa deve definir quem foi o vencedor
# E exibir qual jogada cada jogador escolheu e quem foi o vencedor.

import random

escolhas = ['pedra', 'papel', 'tesoura']

humano = input("Digite pedra, papel ou tesoura! ")
while(humano not in escolhas):
  print("Digite um valor válido, tem de ser pedra, papel ou tesoura! ")
  humano = input("Digite pedra, papel ou tesoura! ")
  jogada_pc = random.choice(escolhas)

if (jogada_pc == 'pedra'):
  if (humano == 'papel'):
    print(f"Parabéns humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você ganhou!")
  else:
    print(f"Poxa vida humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você perdeu!")
elif (jogada_pc == 'papel'):
  if (humano == 'tesoura'):
    print(f"Parabéns humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você ganhou!")
  else:
    print(f"Poxa vida humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você perdeu!")
else:
  if (humano == 'pedra'):
    print(f"Parabéns humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você ganhou!")
  else:
    print(f"Poxa vida humano! Você escolheu {humano}, e o pc escolheu {jogada_pc}, ou seja, você perdeu!")
