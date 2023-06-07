import random

def play_game():
    print("Vamos jogar Pedra, papel tesoura")
    print("Digite sua escolha: pedra, papel, ou tesoura")

    choices = ["pedra", "papel", "tesoura"]
    user_choice = input().lower()

    if user_choice not in choices:
        print("Escolha inválida. Por favor tente novamente.")
        play_game()

    computer_choice = random.choice(choices)
    print("O Computador escolheu:", computer_choice)

    if user_choice == computer_choice:
        print("É um empate!")
    elif (
        (user_choice == "pedra" and computer_choice == "tesoura") or
        (user_choice == "papel" and computer_choice == "pedra") or
        (user_choice == "tesoura" and computer_choice == "papel")
    ):
        print(f"Você escolheu {user_choice}, o computador escolheu {computer_choice}")
        print("Você venceu!")
    else:
        print(f"Você escolheu {user_choice}, o computador escolheu {computer_choice}")
        print("Você perdeu!")

    play_again()

def play_again():
    print("Você quer jogar de novo? (sim or não)")
    choice = input().lower()

    if choice == "sim":
        play_game()
    elif choice == "não":
        print("Obrigado por jogar!")
    else:
        print("Escolha inválida. Tente novamente.")
        play_again()

play_game()
