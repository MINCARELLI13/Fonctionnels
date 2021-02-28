# -*- coding: utf8 -*-
import json
import time

class A:
    def increment(self, i):
        print('Dans la classe A, i =', i)

# Dans la classe "B()", la méthode "super()" permet d'appeler la méthode "increment()" de la classe A
class B(A):
    def increment(self, i):
        print('Dans la classe B, i =', i)
        super().increment(i + 1)    # la méthode "super()" permet d'appeler la méthode "increment()" contenue dans la classe parent "A()"
                                    # ceci revient à : "A.increment(self, i + 1)"  (attention au "self" en plus !)

# Dans la classe "C()", la méthode "super()" permet d'appeler la méthode "increment()" de la classe B
class C(B):
    def increment(self, i):
        print('Dans la classe C, i =', i)
        super().increment(i+1)      # la méthode "super()" permet d'appeler la méthode "increment()" contenue dans la classe parent "B()"
                                    # ceci revient à : "B.increment(self, i + 1)"  (attention au "self" en plus !)

if __name__ == '__main__':
    print("")
    c = C()
    c.increment(1)
