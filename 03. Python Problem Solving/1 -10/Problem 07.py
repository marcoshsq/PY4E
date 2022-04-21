# Como listar todos os arquivos de um diretório em Python.

from os import listdir
from os.path import isfile, join

lista_file =  [f for f in listdir("\Users") if isfile(join("\Users", f))]