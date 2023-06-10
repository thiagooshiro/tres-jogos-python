# Desafio 1:

# Vamos criar um jogo de advinhação.
# O Computador irá escolher de forma aleatória um número entre 1 e 100.
# O jogador deve tentar adivinhar o número
# Apenas valores numéricos são válidos.

#importando random
import random

mystery = random.randint(1,100)

while (True):

    try:
      tentativa = int(input("Tente adivinhar o número! Lembre que você deve inserir um número de 1 a 100! "))
    except ValueError:
        tentativa = print("Você inseriu um valor inválido, precisamos de um número entre 1 a 100!")
    else:
        if tentativa in range(1,100):
          if tentativa == mystery:
            print(f"Parabéns, o número misterioso é {mystery}!")
            break
          else:
            print("Você não adivinhou o número, tente novamente!")
        else:
            print("Você não inseriu um número entre 1 a 100, tente novamente! ")

    

