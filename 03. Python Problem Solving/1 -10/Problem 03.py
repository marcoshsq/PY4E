# Como saber quanto tempo um programa demorou para ser executado.

import time


def temp_exec():
    """Essa função realiza uma soma simples, mas dentro
    dela temos um contados de tempo, onde começamos a contar
    no inicio e no fim, depois pegamos a diferença para saber
    quanto tempo demorou para rodar o programa!
    Cool u.u"""
    temp_inicio = time.time()
    s = 0
    for i in range(1, n + 1):
        s += i

    temp_fim = time.time()
    return s, temp_fim - temp_inicio


n = 1
print(temp_exec())
