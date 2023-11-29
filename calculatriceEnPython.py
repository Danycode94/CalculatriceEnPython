"""
C'est un programme qui permet de calculer la moyenne des notes entrer par l'utilisateur.
"""

my_list = []

nombre_iterations = input("Saisir la quantite de notes: ").strip()
print("\n")

if nombre_iterations:
    
    """ Verifier que le nombre entrer est un nombre positif et non null. """
    while(int(nombre_iterations) <= 0 ):
        nombre_iterations = int(input("La quantite de notes doit etre positif: ").strip())
        
    for item in range(int(nombre_iterations)):
        note = int(input(f"Saisir la note #{(item + 1)} : ").strip())
        my_list.append(note)
        
    """ Calcul de la moyenne des notes dans la liste. """
    somme = 0
    for item in my_list:
        somme += item
        
    moyenne = somme/len(my_list)
    print(f"\nVotre moyenne est de: {moyenne}")
    
    """ Verifier les mentions pour la moyenne. """
    if moyenne >= 90:
        print("Vous avez obtenir 'A' comme mention\n")
    elif moyenne >= 80 and moyenne < 90:
        print("Vous avez obtenir 'B' comme mention\n")
    elif moyenne >= 70 and moyenne < 80:
        print("Vous avez obtenir 'C' comme mention\n")
    elif moyenne >= 60 and moyenne < 70:
        print("Vous avez obtenir 'D' comme mention\n")
    elif moyenne < 60 :
        print("Vous avez obtenir 'F' comme mention\n")     
        
else:
    print("Vous n'avez saisie aucun nombre \n")
