# MODELE : import de fonctions et de variables internes
from modele.api.getDatasApi import getDatasApi
from modele.config import apiHackathonsProjets
from views.tools_views import printProjetsHackathon

def ctrl_choix_2_les_projets_hackathon():
    # CONTROLEUR
    hackathonsProjets = getDatasApi(apiHackathonsProjets)
    # print(hackathonsProjets)

    # VUE
    print("choix 2 : les projets par hackathon")
    printProjetsHackathon(hackathonsProjets)