secret_word = "Secret"
guess = ""
tries = 0

while (guess != secret_word and tries < 3):
    guess = input("Enter your guess: ")
    tries += 1

if guess == secret_word and tries <= 3:
    print("You win!")

elif tries >= 3:
    print("You lose!")