# Extra Exercise 011

'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''


file_size = float(input('Insert the size of the file (MB):'))
internet_speed = float(input('Insert the velocity of your net (Mbps): '))
bit_to_byte = internet_speed / 8
download_time = (file_size / bit_to_byte) / 60
print(f'O tempo de download será de {download_time:.2f}min')
