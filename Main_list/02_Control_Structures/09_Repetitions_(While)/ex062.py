# Exercício Python #062 - Super Progressão Aritmética v3.0
'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro_termo = int(input('Qual o primeiro termo da Progressão Aritmética: '))
razao = int(input('Qual a razão de progressão: '))
termo = primeiro_termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        c += 1

    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'O número total de termos foi {total}')
print('FIM')
