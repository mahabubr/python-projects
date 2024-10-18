import random

def number_guessing_game():
    number_guess = random.randint(1, 100)
    attempts = 0

    print("Wellcome to number guessing game")
    print("Please select a number between 1 to 100")

    while True:
        try:
            guess = int(input("Enter your gess: "))

            if guess < number_guess:
                print("Too low")
            elif guess > number_guess:
                print("Too High")
            else :
                print("Congratulations. your guessing number is correct")
                break
        except ValueError:
            print("Please enter valid number")


if __name__ == "__main__":
    number_guessing_game()