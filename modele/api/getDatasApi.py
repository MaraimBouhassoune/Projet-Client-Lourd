# import de modules externes python : pip install requests pour l'installer
import requests

# import de mes fonctions et mes données
from modele.config import site

def getDatasApi(api) : 
    url = site + "/" + api
    # print(url)

    try:
        datasStringJSON = requests.get(url)
        if datasStringJSON.status_code != 200:
            print("L'adresse du site n'est pas valide.")
            exit()
    except Exception as e:
        print(f"Accès au serveur impossible : {e}")
        exit()
    
    datasPython = datasStringJSON.json()
    return datasPython
