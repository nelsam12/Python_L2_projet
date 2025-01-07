
import os
def menu_gestionnaire() -> int:
    """
    Cette fonction affiche le menu du gestion

    Returns:
        int: @
    """
    while True:
        print("==========Menu Gestionnaire==========")
        print("1 - Créer un opérateur")
        print("2 - Renommer un opérateur")
        print("3 - Lister les opérateurs et leur index")
        print("4 - Lister les numéros d'un opérateur")
        print("5 - Ajouter un nouvel index pour un operateur existant")
        print("6 - Supprimer un index d’un operateur")
        print("7 - Vendre un numéro")
        print("8 - Vendre du crédit a un client")
        print("9 - État de la caisse ")
        print("10 - Quitter")
    
        choice = input("votre choix : ")
        if not check_input(choice=choice):
            display_error(choice)
            continue
        else:
            return int (choice)
    
    

# def check_input(choice : str) -> bool:
#     return choice.isdigit()

check_input = lambda choice : choice.isdigit()

clear = lambda : os.system('cls')
pause = lambda : os.system('pause')

def display_error(choice : str, message : str = "Vous devez saisir un entier") -> int:
    if not (check_input(choice)):
        print(message)
        pause()
        clear()
    else:
        return int(choice)
    
    
def question(sms) -> bool:
    while True:
        rep = input(sms + " (oui/non): ").strip().lower()
        if rep == "oui":
            return True
        elif rep == "non":
            print("Action terminée. Merci!")
            return False
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")