from fileinput import filename

from tabulate import tabulate
from termcolor import colored
from Controllers.Operateur import generer_numeros_telephones
from Models.Operateur import controle_index, verifier_existence
from Views.Functions import question
from const import FILE_NAME_OPERATOR


def create_operateur():
    nom = input("Entrez le nom de l'opérateur :\n")
    if verifier_existence(FILE_NAME_OPERATOR, nom, "nom"):
        print(f"L'opérateur '{nom}' existe déjà.")
        return
    Indexes=[]
    while True:
        # 77 |78 |...
        Indexe = controle_index()
        Indexes.append(Indexe)
        if not (question("Voulez-vous un index?")):
            break
    # 77,78,70,...
    indexes_joined = (",").join(Indexes)
    Credit = get_positif("Entrez le total de crédit de l'operateur :\n")
    Tarif1 = input("Entrez le tarif d'appel des numeros du mm operateur :\n")
    Tarif2 = input("Entrez le tarif d'appel des numeros du mm operateur :\n")
    prefixe = "+221"
    nombre = 10 
    Numeros = []
    for index in Indexes:
        Numeros.extend(generer_numeros_telephones(prefixe, index, nombre))
    operateur = f"{nom}:{indexes_joined}:{Credit}:{Tarif1}:{Tarif2}:{Numeros}\n"
    return operateur


positif =  lambda x : x > 0


def get_positif(message : str) -> int | float:
    while True:
        value = input(message)
        if not (value.isdigit()):
            continue
        if int (value) < 0:
            continue
        return int (value)
    
    
#
def read_and_display_operator_data(filename = FILE_NAME_OPERATOR):
    # Préparer les données pour le tableau
    headers = ["Operateur", "Prix", "Crédit", "Tarif1", "Tarif2"]
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) >= 6:
                row = [
                    parts[0],           # Opérateur
                    parts[1],           # Prix
                    parts[2],           # Crédit
                    parts[3],           # Tarif 1
                    parts[4],           # Tarif 2
                 
                ]
                matrix.append(row)
    
    # Afficher le tableau formaté
    print(tabulate(matrix, headers=headers, tablefmt="rounded_grid"))


def list_operator_numbers(filename = FILE_NAME_OPERATOR):
    print("\nOpérateurs disponibles:")
    operators = []
    
    with open(filename, 'r') as file:
        for line in file:
            operator = line.split(':')[0]
            operators.append(operator)
            print(f"- {operator}")
    
    operator_choice = input("\nEntrez le nom de l'opérateur: ")
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if parts[0].lower() == operator_choice.lower():
                numbers = eval(parts[5])
                # Simuler des numéros vendus (à remplacer par votre logique réelle)
                sold_numbers = numbers[:3]  # Pour l'exemple, les 3 premiers sont "vendus"
                sold_numbers_bool = [n.endswith('v') for n in numbers]
                # Préparer les données pour tabulate
                table_data = []
                row = []
                for i, num in enumerate(numbers, 1):
                    # Colorer le numéro en rouge si vendu, vert si disponible
                    formatted_num = colored(num, "black", "on_red" if num in sold_numbers else "on_green")
                    
                    # formatted_num = colored(num, "black", "on_red" if num in sold_numbers else "on_green")

                    row.append(f"({i:03d}) {formatted_num}")
                    
                    if len(row) == 4:  # 4 colonnes par ligne
                        table_data.append(row)
                        row = []
                
                # Ajouter la dernière ligne si incomplète
                if row:
                    while len(row) < 4:
                        row.append("")
                    table_data.append(row)
                
                # Afficher le tableau
                headers = ["Numero", "Numero", "Numero", "Numero"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                return
                
        print("Opérateur non trouvé!")