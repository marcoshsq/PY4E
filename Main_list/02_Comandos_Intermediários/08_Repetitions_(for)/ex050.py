# Exercício Python 050 - Soma dos pares

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''


soma = 0
for i in range(0, 6):  
    num = int(input('Insira um número inteiro: '))  # Como o input está dentro do laço com o range de 0 à 6, ele repete a pergunta 6x u.u
    if num % 2 == 0 :     # Se o número posto dentro de num didido por dois tem resto zero;
        soma += num       # Ele entra na soma
        
print(f'A soma é {soma}')


