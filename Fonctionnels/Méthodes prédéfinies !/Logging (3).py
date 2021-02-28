# -*- coding: utf8 -*-
#!/usr/bin/python
import logging

# Le but du module "logging" est de remplacer le fameux teste "print("...")" mais en étant plus précis
# Pour cela, il y a 5 niveaux de messages : Debug, Info, Warning, Error, Critical

# on configure le module pour qu'il affiche tous les messages à partir de "Debug"
# (par défaut, il n'affiche rien en-dessous de "Warning")
logging.basicConfig(level=logging.DEBUG)


logging.warning("coin")     # on affiche le résultat "coin" mais en mode "Warning"
logging.debug("pan !")       # on affiche le résultat "pan !"  en mode "Debug"