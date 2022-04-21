# Como fazer um perfil de um script Python.

import cProfile

def soma():
    print(1, 3)

cProfile.run("soma()")