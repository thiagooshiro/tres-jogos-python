import random
from fruitlist import fruits

def play_hangman():
    word_list = fruits
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    attempts = 6

    print("Vamos jogar Forca")
    print("A palavra contém", len(secret_word), "letras.")

    play_round(secret_word, guessed_letters, attempts)

def play_round(secret_word, guessed_letters, attempts):
    if attempts == 0:
        print("Game Over! Acabaram suas tentativas!!!")
        print("A palavra secreta era:", secret_word)
        return

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if display_word.replace(" ", "") == secret_word:
        print("Parabéns! Você adivinhou corretamente.")
        return

    guess = input("Digite uma letra: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Entrada inválida. Por favor digite apenas uma letra.")
        play_round(secret_word, guessed_letters, attempts)
        return

    if guess in guessed_letters:
        print("Você já tentou essa letra. Tente novamente.")
        play_round(secret_word, guessed_letters, attempts)
        return

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts -= 1
        if attempts == 0:
            print('É o fim...')
        else:
            print("Você errou. Ainda restam", attempts, "tentativas...")

    play_round(secret_word, guessed_letters, attempts)

play_hangman()
