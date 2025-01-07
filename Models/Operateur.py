from const import FILE_NAME_NUMERO, FILE_NAME_OPERATOR, MODE_AJOUT, MODE_ECRITURE, MODE_OUVERTURE



# def get_value_operateur(ligne: int, position:int):
#     l = ligne.split(":")
#     Nom_Op = l[int]
#     return Nom_Op


def get_nom_operateur(ligne) -> str:
    l = ligne.split(":")
    Nom_Op = l[0]
    return Nom_Op

def get_index_operateur(ligne):
    l = ligne.split(":")
    Index_op = l[1]
    return Index_op

def get_credit_operateur(ligne) -> int:
    l = ligne.split(":")
    Credit_op = l[2]
    return int(Credit_op)

def get_tarif1_operateur(ligne):
    l = ligne.split(":")
    Tarif1_op = l[3]
    return int(Tarif1_op)

def get_tarif2_operateur(ligne) -> int:
    l = ligne.split(":")
    Tarif2_op = l[4]
    return int(Tarif2_op)
 
def get_numeros_operateur(ligne) -> list:
    l = ligne.split(":")
    numeros_str = ligne.split(":")[5]
    numeros_op = eval(numeros_str)
    return numeros_op
 

def controle_index():
    tab_index = []
    Index = input("Entrez l'index de l'opérateur (un nombre à 2 chiffres) :\n")
    while not Index.isdigit() or len(Index) != 2:
        print("Index invalide: Votre index doit contenir exactement deux chiffres.\n")
        Index = input("Entrez l'index de l'opérateur (un nombre à 2 chiffres) :\n")
    tab_index.append(Index)
    return Index

def verifier_existence(filename, valeur, champ):
    with open(filename, MODE_OUVERTURE) as f:
        for ligne in f:
            if champ == "nom" and valeur == get_nom_operateur(ligne):
                return True
            elif champ == "index" and valeur in get_index_operateur(ligne).split(","):
                return True
    return False


def save_operator(operateur, filename = FILE_NAME_OPERATOR) -> None: 
    try:
        with open(filename, MODE_AJOUT) as f:
            f.write(operateur)
            print("Opérateur ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'opérateur : {e}")


# def Add_operateur(filename, modeAjout): 
#     try:
#         with open(filename, modeAjout) as f:
#             contenu = Create_operateur()
#             f.write(contenu)
#             print("Opérateur ajouté avec succès.")
#     except Exception as e:
#         print(f"Erreur lors de l'ajout de l'opérateur : {e}")

# def Read_file(filename):
#     try:
#         with open(filename, 'r') as f:
#             print("Contenu du fichier :")
#             print(f.read())
#     except FileNotFoundError:
#         print(f"Le fichier {filename} n'existe pas.")
#     except Exception as e:
#         print(f"Erreur lors de la lecture du fichier : {e}")

# def liste_operateur(filename,modeOuverture):
#     with open(filename,modeOuverture) as f:
#         cpt = 0
#         for ligne in f:
#             cpt = cpt + 1
#             Nom_op =  get_nom_operateur(ligne)
#             Index_op = get_index_operateur(ligne)
#             print(f"{cpt}.Nom Operateur : {Nom_op}")
#             print(f"{cpt}.Index Operateur  : {Index_op}")
#             print("-"*50)

# def liste_numero_operateur(filename,modeOuverture):
#     with open(filename,modeOuverture) as f:
#         for ligne in f:
#             Nom_op =  get_nom_operateur(ligne)
#             Numeros_op = get_numeros_operateur(ligne)
#             print(f"Nom operateur : {Nom_op}")
#             for numero in Numeros_op:
#                 print(numero)
#                 print("-" * 50)

# def operateur_modifier(filename,modeOuverture):
#     operateur_modifier = None
#     nom = input("Entrez le nom de l'operateur dont vous voulez modifier le nom: ")
#     with open(filename,modeOuverture) as f:
#         nouvelles_lignes = []
#         for ligne in f:
#             if(nom == get_nom_operateur(ligne)):
#                 new_nom = input("Entrez le nouveau nom de l'operateur: ")
#                 index = get_index_operateur(ligne)
#                 credit = get_credit_operateur(ligne)
#                 tarif1 = get_tarif1_operateur(ligne)
#                 tarif2 = get_tarif2_operateur(ligne)
#                 numeros = get_numeros_operateur(ligne)
#                 operateur_modifier = f"{new_nom}:{index}:{credit}:{tarif1}:{tarif2}:{numeros}"
#                 nouvelles_lignes.append(operateur_modifier)
#             else:
#                 nouvelles_lignes.append(ligne)
#         if (operateur_modifier is None):
#             print("Cet operateur n'existe pas")
#         else:
#             with open(filename,MODE_ECRITURE) as f:
#                 f.writelines(nouvelles_lignes)
#                 print("L'operateur a été renommer avec succes.")

# def Vente():
#     credit = int(input("Entrez le prix du credit à vendre :\n"))
#     return credit

# def vendre_credit(filename, modeOuverture):
#     nom = input("Entrez le nom de l'operateur dont vous voulez vendre du credit: \n")
#     operateur_trouve = False  
#     with open(filename, modeOuverture) as f:
#         new_vente = []
#         for ligne in f:
#             if nom == get_nom_operateur(ligne):
#                 operateur_trouve = True  
#                 credit_a_vendre = Vente()
#                 credit = int(get_credit_operateur(ligne)) - credit_a_vendre
#                 if credit < 0:
#                     print(f"Crédit insuffisant pour l'opérateur {nom}.")
#                     new_vente.append(ligne)
#                 else:
#                     vente = ligne.strip().split(":")
#                     vente[0] = nom
#                     vente[1] = get_index_operateur(ligne)
#                     vente[2] = str(credit)
#                     vente[3] = get_tarif1_operateur(ligne)
#                     vente[4] = get_tarif2_operateur(ligne)
#                     new_vente.append(":".join(vente) + "\n")
#             else:
#                 new_vente.append(ligne)

#     if not operateur_trouve:
#         print(f"L'opérateur {nom} n'existe pas.")
#     else:
#         with open(filename, MODE_ECRITURE) as f:
#             f.writelines(new_vente)
#             print("La vente a été effectuée avec succès.")


# def supp_index(filename, modeOuverture, modeEcriture):
#     nom = input("Entrez le nom de l'opérateur dont vous voulez supprimer un index :\n")
#     index_a_supprimer = input("Entrez l'index à supprimer :\n")
#     with open(filename, modeOuverture) as f:
#         nouvelles_lignes = []
#         for ligne in f:
#             if nom == get_nom_operateur(ligne):
#                 indexes = get_index_operateur(ligne).split(",")
#                 if index_a_supprimer in indexes:
#                     indexes.remove(index_a_supprimer)
#                     indexes_str = ",".join(indexes)
#                     nouvelle_ligne = f"{nom}:{indexes_str}:{get_credit_operateur(ligne)}:{get_tarif1_operateur(ligne)}:{get_tarif2_operateur(ligne)}:{get_numeros_operateur(ligne)}\n"
#                     nouvelles_lignes.append(nouvelle_ligne)
#                     print(f"L'index {index_a_supprimer} a été supprimé pour l'opérateur {nom}.")
#                 else:
#                     print(f"L'index {index_a_supprimer} n'existe pas pour l'opérateur {nom}.")
#                     nouvelles_lignes.append(ligne)
#             else:
#                 nouvelles_lignes.append(ligne)
    
#     with open(filename, modeEcriture) as f:
#         f.writelines(nouvelles_lignes)
#         print("Mise à jour effectuée avec succès.")

# def add_index(filename, modeOuverture, modeEcriture):
#     nom = input("Entrez le nom de l'opérateur auquel vous voulez ajouter un index :\n")
#     index_a_ajouter = Controle_index()  
#     if verifier_existence(filename, index_a_ajouter, "index"):
#         print(f"L'index '{index_a_ajouter}' existe déjà.")
#         return
#     with open(filename, modeOuverture) as f:
#         nouvelles_lignes = []
#         index_trouve = False
#         for ligne in f:
#             if nom == get_nom_operateur(ligne):
#                 index_trouve = True
#                 indexes = get_index_operateur(ligne).split(",")
#                 if index_a_ajouter in indexes:
#                     print(f"L'index {index_a_ajouter} existe déjà pour l'opérateur {nom}.")
#                     nouvelles_lignes.append(ligne)
#                 else:
#                     indexes.append(index_a_ajouter)
#                     indexes_str = ",".join(indexes)
#                     prefixe = "+221"
#                     nouveaux_numeros = generer_numeros_telephones(prefixe, index_a_ajouter, 10)
#                     numeros_existants = get_numeros_operateur(ligne)
#                     numeros_totaux = numeros_existants + nouveaux_numeros

#                     nouvelle_ligne = f"{nom}:{indexes_str}:{get_credit_operateur(ligne)}:{get_tarif1_operateur(ligne)}:{get_tarif2_operateur(ligne)}:{numeros_totaux}\n"
#                     nouvelles_lignes.append(nouvelle_ligne)
#                     print(f"L'index {index_a_ajouter} et ses 10 numéros ont été ajoutés à l'opérateur {nom}.")
#             else:
#                 nouvelles_lignes.append(ligne)
#         if not index_trouve:
#             print(f"L'opérateur '{nom}' n'existe pas.")
#     with open(filename, modeEcriture) as f:
#         f.writelines(nouvelles_lignes)
#         print("Mise à jour effectuée avec succès.")

# def vente_numero(filename, filenamenumero, modeOuverture, modeEcriture):
#     nom = input("Entrez le nom de l'opérateur dont vous voulez vendre un numéro :\n")
#     numero_vendu = None
#     operateur_trouve = False
#     with open(filename, modeOuverture) as f:
#         lignes_modifiees = []
#         for ligne in f:
#             if nom == get_nom_operateur(ligne):
#                 operateur_trouve = True
#                 numeros = get_numeros_operateur(ligne)
#                 if not numeros:
#                     print(f"Aucun numéro disponible pour l'opérateur {nom}.")
#                     lignes_modifiees.append(ligne)
#                 else:
#                     numero_vendu = numeros.pop(0)
#                     nouvelle_ligne = f"{nom}:{get_index_operateur(ligne)}:{get_credit_operateur(ligne)}:{get_tarif1_operateur(ligne)}:{get_tarif2_operateur(ligne)}:{numeros}\n"
#                     lignes_modifiees.append(nouvelle_ligne)
#             else:
#                 lignes_modifiees.append(ligne)

#     if not operateur_trouve:
#         print(f"L'opérateur {nom} n'existe pas.")
#         return
#     with open(filename, modeEcriture) as f:
#         f.writelines(lignes_modifiees)
#     if numero_vendu:
#         with open(filenamenumero, MODE_AJOUT) as f_vendu:
#             f_vendu.write(f"{nom}:{numero_vendu}\n")
#         print(f"Le numéro {numero_vendu} a été vendu et ajouté au fichier {filenamenumero}.")
#     else:
#         print("Aucun numéro n'a été vendu.")


def vente_numero(filename = FILE_NAME_OPERATOR, filenamenumero = FILE_NAME_NUMERO, modeOuverture = MODE_OUVERTURE, modeEcriture = MODE_ECRITURE):
    nom = input("Entrez le nom de l'opérateur dont vous voulez vendre un numéro :\n")
    numero_vendu = None
    operateur_trouve = False
    with open(filename, modeOuverture) as f:
        lignes_modifiees = []
        for ligne in f:
            if nom == get_nom_operateur(ligne):
                operateur_trouve = True
                numeros = get_numeros_operateur(ligne)
                if not numeros:
                    print(f"Aucun numéro disponible pour l'opérateur {nom}.")
                    lignes_modifiees.append(ligne)
                else:
                    numero_vendu = numeros[0]
                    numeros.pop(0)
                    numeros.append(numero_vendu + "v")
                    nouvelle_ligne = f"{nom}:{get_index_operateur(ligne)}:{get_credit_operateur(ligne)}:{get_tarif1_operateur(ligne)}:{get_tarif2_operateur(ligne)}:{numeros}\n"
                    lignes_modifiees.append(nouvelle_ligne)
            else:
                lignes_modifiees.append(ligne)

    if not operateur_trouve:
        print(f"L'opérateur {nom} n'existe pas.")
        return
    with open(filename, modeEcriture) as f:
        f.writelines(lignes_modifiees)
    if numero_vendu:
        with open(filenamenumero, MODE_AJOUT) as f_vendu:
            f_vendu.write(f"{nom}:{numero_vendu}\n")
        print(f"Le numéro {numero_vendu} a été vendu et ajouté au fichier {filenamenumero}.")
    else:
        print("Aucun numéro n'a été vendu.")







# from tabulate import tabulate

# # Liste des numéros à afficher
# numeros = [
#     '+221703532949', '+221700535617', '+221705076490', '+221708737186',
#     '+221707145247', '+221707079446', '+221704543872', '+221709333299',
#     '+221708951600', '+221701849720', '+221760591539', '+221766243451',
#     '+221767816805', '+221761550067', '+221766176948', '+221760107965',
#     '+221763778704', '+221769667767', '+221765102793', '+221766525680'
# ]

# # Organiser les numéros en lignes de 3 colonnes
# tableau = [numeros[i:i+3] for i in range(0, len(numeros), 3)]

# # Afficher le tableau avec des bordures
# print(tabulate(tableau, tablefmt="grid"))


# Add_operateur(filename, modeAjout)
# Read_file(filename)
# liste_operateur(filename,modeOuverture)
# liste_numero_operateur(filename,modeOuverture)
# operateur_modifier(filename,modeOuverture)
# vendre_credit(filename,modeOuverture)
# supp_index(filename, modeOuverture, modeEcriture)
# add_index(filename, modeOuverture, modeEcriture)
# vente_numero(filename, filenamenumero, modeOuverture, modeEcriture)



