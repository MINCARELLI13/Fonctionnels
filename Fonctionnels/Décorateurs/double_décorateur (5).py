print("")

def pain(func):

    def wrapper():
        func()
        print(" <\______/>")
    return wrapper


def ingredients(func):

    def wrapper():
        func()
        print("  #tomates#")
        print("  ~salade~")
    return wrapper

@pain                                   # ici on cumule 2 décorateurs et on exécute "pain(ingredients(sandwich))""
@ingredients                            # plus exactement on affecte"pain(ingredients(sandwich))" à "sandwich"
def sandwich(food="*champignons*"):     # en faisant sandwich = pain(ingredients(sandwich))
    print(food)

# et on lance sandwich
sandwich()
#output:
#
# *champignons*
#   #tomates#
#   ~salade~
#  <\______/>