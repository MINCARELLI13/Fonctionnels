import random as rd

print()

# on génére 10 chiffres aléatoirement
nombres = [rd.randint(0, 10) for i in range(0, 10)]
print(nombres)

choices = {0:"pair", 1:"impair"}

# on identifie les nombres pairs et les impairs
for i in nombres:
    result = choices.get(i%2, i)    # result = choices.get(key, value) où value = "pair" ou "impair"
    print(result, end=",")

print()