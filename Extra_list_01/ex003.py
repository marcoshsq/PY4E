# Exercício Extra 003: let's Code

'''

Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:

a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.

'''

from termcolor import colored

sim = '1 para SIM'
nao = '0 para NÃO'
print(('Responda com '), colored(sim, 'green'), 'ou', colored(nao, 'red'))

pergunta_01 = int(input('Mora perto da vítima? '))
if pergunta_01 == 1 :
    suspeito = 1
else :
    suspeito = 0

pergunta_02 = int(input('Já trabalhou com a vítima? '))
if pergunta_02 == 1 :
    suspeito = suspeito + 1
else :
    suspeito =  suspeito + 0

pergunta_03 = int(input('Telefonou para a vítima? '))
if pergunta_03 == 1 :
    suspeito = suspeito + 1
else :
    suspeito =  suspeito + 0
    
pergunta_04 = int(input('Esteve no local do crime? '))
if pergunta_04 == 1 :
    suspeito = suspeito + 1
else :
    suspeito =  suspeito + 0
    
pergunta_05 = int(input('Devia para a vítima? '))
if pergunta_05 == 1 :
    suspeito = suspeito + 1
else :
    suspeito =  suspeito + 0
    
if suspeito >= 5 :
    print(colored('Você é o ASSASSINO/A!!!', 'red'))
elif suspeito == 4 or suspeito == 3 :
    print(colored('Você é cúmplice, seu danadinho. u.u', 'yellow'))
elif suspeito == 2 :
    print(colored('Você é suspeito, por enquanto. Iremos investiar mais...', 'blue'))
else :
    print(colored('Você é inocente, por enquanto. Ordináriaaaa...', 'green'))



# Arrumar o código para aceitar valores diferentes de 1 e 0 u.u
