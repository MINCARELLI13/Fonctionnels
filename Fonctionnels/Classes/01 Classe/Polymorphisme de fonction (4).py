# -*- coding: utf8 -*-
import json
import time

# https://o7planning.org/fr/11417/heritage-et-polymorphisme-en-python#

class English:
    
    def greeting(self):       
        print ("Hello")
        
        
class French:
    
    def greeting(self):
        print ("Bonjour")
  
  
def intro(language):
    language.greeting()
    
    
langue_anglaise  = English()
langue_francaise = French()   
 
intro(langue_anglaise)
intro(langue_francaise)