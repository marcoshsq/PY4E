# Como imprimir Data e horário atual em Python.

import datetime

agora = datetime.datetime.now()
print("Agora são: ", agora.strftime("%y-%m-%d %H:%M:%S"))
