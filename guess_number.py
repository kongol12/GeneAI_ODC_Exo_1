import random

number = random.randint(1, 100)

print("Bienvenue dans mon petit jeu Guess the number")  
while True:
    guess = int(input("Devinez le nombre : "))

    if guess < number:
        print("Trop petit")
    elif guess > number:
        print("Trop grand")
    else:
        print("Correct !")
        break