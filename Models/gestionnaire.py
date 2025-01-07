# filenameG = "BD/gestionnaire.txt"
# modeOuverture = 'r'
# modeAjout = 'a'
# modeEcriture = 'w'

# def Get_nom_gestionnaire(ligne):
#     l = ligne.split(":")
#     Nom_Op = l[0]
#     return Nom_Op

# def Get_prenom_gestionnaire(ligne):
#     l = ligne.split(":")
#     Index_op = l[1]
#     return Index_op

# def Get_mdepasse_gestionnaire(ligne):
#     l = ligne.split(":")
#     Credit_op = l[2]
#     return Credit_op


# def creer_gestionnaire():
#     nom = input("Entrez votre nom: \n")
#     prenom = input("Entrez votre prenom: \n")
#     mot_de_passe = input("Entrez votre mot de passe: \n")
#     gestionnaire = f"{nom}:{prenom}:{mot_de_passe}\n"
#     return gestionnaire


# def add_gestionnaire(filenameG, modeAjout): 
#     try:
#         with open(filenameG, modeAjout) as f:
#             gestionnaire = creer_gestionnaire()
#             f.write(gestionnaire)
#             print("Gestionnaire ajouté avec succès.")
#     except Exception as e:
#         print(f"Erreur lors de l'ajout du gestionnaire : {e}")
#     question("Voulez-vous ajouter un autre gestionnaire?")
#     if(question):
#         add_gestionnaire(filenameG, modeAjout)

# def question(sms):
#     while True:
#         rep = input(sms + " (oui/non): ").strip().lower()
#         if rep == "oui":
#             return True
#         elif rep == "non":
#             print("Action terminée. Merci!")
#             break
#         else:
#             print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")



# # def Gerer_Menu_Gestionnaire():
# #     while True:
# #         menu_gestionnaire()
# #         choix_gest = int(input("Entrez votre choix: \n"))
# #         if choix_gest == 1:
# #         #    kkk
# #         elif choix_gest == 2:




# # Add_gestionnaire(filename,modeAjout)