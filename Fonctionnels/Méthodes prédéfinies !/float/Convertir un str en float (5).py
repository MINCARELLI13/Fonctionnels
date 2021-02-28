# -*- coding: utf8 -*-


# transforme nb en "float" y compris en cas d'utilisation d'une virgule
def get_float(nb):
    nb = nb.strip()			                # supprime les espaces début et fin
    if isinstance(eval(nb), tuple):			# s'il y a une virgule, eval(nb) sera un "tuple"
        nb = str(eval(nb)[0]) + "." + str(eval(nb)[1])
        nb = float(nb)
    else:
	    nb =float(nb)
    return nb

if __name__ == '__main__':
    nombre = str(input("Entrez un nombre : "))
    print(f"Le nombre entré est {get_float(nombre)}")