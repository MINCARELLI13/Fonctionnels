

class Hack:

    # ici, on change une partie du comportement de la méthode "len()"
    # en y ajoutant un message 
    def __len__(self):
        print("on a hacké la méthode 'len()'")
        return 123      # en revanche, la méthode spéciale "__len__()" de Python attend une valeur (ici, on a mis "123") 

a = Hack()
print(len(a))   # on a donc détourné la méthode spéciale de Python pour lui ajouter un message à afficher

print("")
print(a.__len__())  # on aurait aussi pu lancer la méthode "__len__()" de cette façon
