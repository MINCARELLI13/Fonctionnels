print("")

def benchmark(func):
    """
    Un décorateur qui affiche le temps qu'une fonction met à s'éxécuter
    """
    import time

    def wrapper(*args, **kwargs):
        t = time.process_time()
        print(func.__name__, time.process_time())
        return func(*args, **kwargs)
 
    return wrapper


def logging(func):
    """
    Un décorateur qui log l'activité d'un script.
    (Ok, en vrai ça fait un print, mais ça pourrait logger !)
    """
    def wrapper(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return wrapper


def counter(func):
    """
    Compte et affiche le nombre de fois qu'une fonction a été exécutée
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        print("{0} a été utilisée: {1}x".format(func.__name__, wrapper.count))
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(phrase):
    return phrase[::-1]


print(reverse_string("Karine alla en Irak"))
print(reverse_string("Sa nana snob porte de trop bons ananas"))
## reverse_string ('Karine alla en Irak',) {}
## wrapper 0.000132
## wrapper a été utilisée: 1x
## karI ne alla eniraK
## reverse_string ('Sa nana snob porte de trop bons ananas',) {}
## wrapper 0.000128
## wrapper a été utilisée: 2x
## sanana snob port ed etrop bons anan aS
