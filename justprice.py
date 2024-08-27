import random

print("Trouver le prix de l'objet X..")
cible = (random.randint(1,10))
# print(f"cible={cible}")

for i in range (5):
    essai = int(input("Votre proposition entre 1 et 10 : "))

    if essai < 1 or essai > 10 :
        print("Erreur,il faut saisir une valeur entre 1 et 10...")
        exit()

    if cible == essai:
        print("Bravo!!!")
        break
    elif cible < essai:
        print("Trop élevé...")

    else:
        print("Trop peu ...")
print ("Fin du jeu...")