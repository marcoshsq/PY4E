# Exercício Python #058 - Jogo da Adivinhação v2.0

'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.'''

import random
import time

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

computer_guess = random.randint(0, 10) # Faz o computador escolher um número
user_guess = int(input('Em que número eu pensei? ')) # Número do jogador
print('Processando...')   
time.sleep(1)  # Essa funçãp vem com o pacote time e ele deixa eu colocar um time no meu código
counter = 0
while user_guess != computer_guess:
    user_guess = int(input('Humm, não foi dessa vez. Por que não tenta de novo? '))
    print('Processando...')   
    time.sleep(1)
    counter += 1       


if counter <= 1:
    print(f'Parabéns, você é muito bom, só precisou de {counter} tentativa')
elif 1 < counter < 3:
    print(f'Parabéns, você precisou de {counter} tentativas')
else:
    print(f'Você conseguiu, precisou de {counter} tentativas, mas conseguiu.')