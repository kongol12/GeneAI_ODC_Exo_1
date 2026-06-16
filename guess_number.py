import random
#le programme génère un nombre aléatoire entre 1 et 100
number = random.randint(1, 100)

print("Bienvenue dans mon petit jeu Guess the number")
while True:
    guess = int(input("Devinez le nombre : "))

    if guess < number:
        print("Le Nombre est Trop petit")

    elif guess > number:
        print("Le Nombre est Trop grand")
    else:
        print("Correct !")
        break
    #le programme continue à demander à l'utilisateur de deviner jusqu'à ce qu'il trouve le bon nombre