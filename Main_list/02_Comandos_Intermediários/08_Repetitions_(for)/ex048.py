# Exercício Python 048 - Soma ímpares múltiplos de três

'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500'''

soma = 0        # Acumulador é esse valor para fazer contas
contagem = 0    # Acumulador é esse valor para fazer contas
for i in range(1, 501, 2):
    if i % 3 == 0:
        contagem += 1    # Essa syntax de += diz que: ''a = a + b'' é igual á ''a += b'' 
        soma += i
print(f'A soma entre os {contagem} números é {soma}')
