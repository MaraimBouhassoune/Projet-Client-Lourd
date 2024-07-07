def printHackathons(hackathonsProjets):
	# Affichage des infos : 
	print(f"-----------------------------------------------------------")
	print(
		f"|{'idHackathon':>12s} "
		f"|{'nom':>20s} "
		f"|{'dateDebut':>20s} "
		f"| "
	)
	print(f"-----------------------------------------------------------")
	for hackathonProjets in hackathonsProjets: 
		idHackathon = hackathonProjets['idHackathon']
		nomHackathon = hackathonProjets['nom']
		dateDebutHackathon = hackathonProjets['dateDebut']
		print(
			f"|{idHackathon:12} "
			f"|{nomHackathon:>20s} "
			f"|{dateDebutHackathon:>20} "
			f"| "
		)
	print(f"-----------------------------------------------------------")

def printProjetsHackathon(hackathonsProjets):
# version 2 : avec les projets
	print(f"----------------------------------------------------------------------------------------------------------------------------------")
	print(
		f"| {'IDHackathon':>11s} "
		f"| {'nomHackathon':>20s} "
		f"| {'idProjet':>8s} "
		f"| {'nomProjet':>20s} "
		f"| {'pdfProjet':>23s} "
		f"| {'retenu':>6s} "
		f"| {'description':>20s} "
		f"| "
	)
	print(f"----------------------------------------------------------------------------------------------------------------------------------")
	for hackathonProjets in hackathonsProjets: 
		idHackathon = hackathonProjets['idHackathon']
		nomHackathon = hackathonProjets['nom']
		projetsHackathon = hackathonProjets['lesProjets']
		for projetHackathon in projetsHackathon: 
			idProjet = projetHackathon['idProjet']
			nomProjet = projetHackathon['nom']
			pdfProjet = projetHackathon['pdf']
			descriptionProjet = projetHackathon['description']
			retenuProjet = projetHackathon['retenu']
			# on utilise cette variable pour montrer son usage dans une f string
			maxNomHackathon = 20
			print(
				f"| {idHackathon:11} " # 11 c'est nb char de idHackathon = max de la colonne
				f"| {nomHackathon:>{maxNomHackathon}s} " # 20 c'est le max choisi pour la coonne		
				f"| {idProjet:8} " # 8 c'est nb char de idProjet = max de la colonne
				f"| {nomProjet:>20s} "
				f"| {pdfProjet:23s} "
				f"| {retenuProjet:6} " # 6 c'est nb char de retenuProjet = max de la colonne
				f"| {descriptionProjet:>20s} "
				f"| "
			)
	print(f"----------------------------------------------------------------------------------------------------------------------------------")
	