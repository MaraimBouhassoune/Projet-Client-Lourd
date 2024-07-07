# import de modules externes python : pip install requests pour l'installer
import requests

# import de modules natifs du python : ils sont là par défaut
import os

# MODELE : import de fonctions et de variables internes
from modele.api.getDatasApi import getDatasApi
from modele.config import apiHackathonsProjets
from modele.config import site, pdfProjetsHackathon

def ctrl_choix_3_les_pdf_de_tous_projets():
    # CONTROLEUR + VUE (affichage en cours de travail)
    print()
    print("Création du dossier :", pdfProjetsHackathon)
    os.makedirs(pdfProjetsHackathon, exist_ok=True)

    hackathonsProjets = getDatasApi(apiHackathonsProjets)

    print("Chargement des fichiers de projets et création des dossiers hackahton")
    for hackathonProjets in hackathonsProjets: 
        nomHackathon = hackathonProjets['nom']
        os.makedirs(pdfProjetsHackathon+"/"+nomHackathon, exist_ok=True)
        print("    Création du dossier du hackathon :", pdfProjetsHackathon+"/"+nomHackathon)
        projetsHackathon = hackathonProjets['lesProjets']
        for projetHackathon in projetsHackathon: 
            # on récupère le nom du pdf par l'api
            pdfProjet = projetHackathon['pdf']
            # on crée l'url correspondant au pdf
            url = site + "/public/pdf/" +  pdfProjet
            # on charge le fichier : c'est des datas binaires
            try:
                response = requests.get(url)
                datasBinPdf = response.content
            except Exception as e:
                print(f"Accès au serveur impossible : {e}")
                exit()
            # on enregistre les datas binaires dans un fichier au nom du projet dans le dossier du hackathon
            chemin_et_nom_du_fichier = pdfProjetsHackathon+"/"+nomHackathon+"/"+pdfProjet
            print("        Création du projet :", chemin_et_nom_du_fichier)
            with open(chemin_et_nom_du_fichier, "wb") as f: 
                f.write(datasBinPdf)

