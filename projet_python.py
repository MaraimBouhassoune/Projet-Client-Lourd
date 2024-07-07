# import de bibliothèques natives du Python
from sys import platform # platform est une variable
from os import system 
# usage : soit os.system soit system :
#       attention : os.system ne marche pas sur PC : on évite !

# import de fonctions de notre projet en mode MVC
#    dossier.fichier.py      import fonction()
from ctrls.ctrl_choix_0_help import ctrl_choix_0_help
from ctrls.ctrl_choix_1_les_hackathons import ctrl_choix_1_les_hackathons
from ctrls.ctrl_choix_2_les_projets_hackathon import ctrl_choix_2_les_projets_hackathon
from ctrls.ctrl_choix_3_les_pdf_de_tous_projets import ctrl_choix_3_les_pdf_de_tous_projets


if platform == "win32" :
    system("cls") # sur PC
else : # forcément linux : ["linux", "linux2"]
    system("clear") # sur MAC

while(True):
    print()
    print("-----------------------------------------------------")
    print("choix 0 ou h ou help : afficher l'aide")
    print()
    print("choix 1 : afficher les hackathons")
    print("choix 2 : afficher les projets")
    print("choix 3 : télécharger les pdf des projets")
    print()
    print("choix q ou Q : quitter")
    print("-----------------------------------------------------")
    choix = input("Entrez votre choix : ")
    print("-----------------------------------------------------")
    print()

    if (choix in ["q", "Q", "quitter"]):
        print("au revoir")
        exit()
    elif (choix in ["0", "h", "?", "help"]): ctrl_choix_0_help()
    elif (choix == "1"): ctrl_choix_1_les_hackathons()
    elif (choix == "2"): ctrl_choix_2_les_projets_hackathon()
    elif (choix == "3"): ctrl_choix_3_les_pdf_de_tous_projets()
    else:
        print("mauvais choix")