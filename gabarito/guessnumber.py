import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Bem vindo ao jogo da advinhação")
    print("Estou pensando em um número entre 1 e 100")

    while True:
        guess = int(input("Em qual número estou pensando? "))
        attempts += 1

        if guess == secret_number:
            print("Parabéns! Você adivinhou o número corretamente.")
            print("Só levou", attempts, "tentativa(s) para você advinhar")
            break
        elif guess < secret_number:
            print("Muito baixo! Tá mais pra cima")
        else:
            print("Muito alto! Tá mais pra baixo.")

guess_the_number()
