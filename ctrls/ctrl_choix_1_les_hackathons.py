## MODELE : import de fonctions et de variables internes
from modele.api.getDatasApi import getDatasApi
from modele.config import apiHackathonsProjets
from views.tools_views import printHackathons

def ctrl_choix_1_les_hackathons():
    # CONTROLEUR
    hackathonsProjets = getDatasApi(apiHackathonsProjets)

    # VUE
    print("choix 1 : les hackathons")
    printHackathons(hackathonsProjets)