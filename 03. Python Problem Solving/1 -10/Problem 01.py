# Como encontrar a média de qualquer N números em Python:

numero = int(input("Quantos números: \n"))  # Quantos números terá a média.
soma_total = 0  # Nossa soma será armazenada aqui.

for i in range(numero):
    """Basicamente, estamos criando um for loop, onde
    a função range recebe como parâmetro aquele número
    que o user escolher.

    Dentro do loop colocamos outro input de valores a
    serem somados, onde em cada iteração, esse input
    é somado na nossa variável."""
    valores = int(input("Valor a ser somado: \n"))
    soma_total += valores

# Por último, tiramos a média e profit!
media = soma_total / numero  # Cálculo da média.
print(f"A média dos valores é: {media:.2f}")
