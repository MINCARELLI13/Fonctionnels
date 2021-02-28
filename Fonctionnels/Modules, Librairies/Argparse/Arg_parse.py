import argparse

# Ce script permet de lancer n'importe quel programme ou script à partir d'une console
# Une fois le code ci-dessous inséré dans un script, on peut alors lancer le script "à partir d'une console"
# en spécifiant des paramètres particuliers comme le nom d'un fichier à analyser ou l'extension du fichier à prendre en compte

parser = argparse.ArgumentParser()

parser.add_argument('name', help="nom de l'utilisateur")

parser.add_argument('-g', '--greetingggg', default='Hello', help='salutation alternative (facultative)')

args = parser.parse_args()

print("{salutation}, {name} !".format(salutation=args.greetingggg, name=args.name))

# pour lancer le script "Argparse.py" : aller dans "GitBash" et taper la commande "python Arg_parse.py  Sergio"  --> "Hello Sergio"
# si vous taper "python Arg_parse.py Sergio -g Salut "  --> "Salut Sergio"