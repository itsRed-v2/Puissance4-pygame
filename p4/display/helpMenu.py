import os

from p4.utils.color import Color

def displayHelp():
	print(f"""
=== HELP ===

Pour jouer un jeton, entrez le numéro de la colonne que vous voulez jouer

{Color.BOLD}Commandes:{Color.RESET}
\"stop\" stoppe le programme
\"help\" affiche ce menu
""")

	size = os.get_terminal_size()
	for i in range(size.lines - 10):
		print("")

	print("Appuyez sur Entrée pour revenir au jeu""")
	input("-> ")