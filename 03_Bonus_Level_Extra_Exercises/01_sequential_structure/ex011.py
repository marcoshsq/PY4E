# Extra Exercise 011

'''Make a program that asks for the size of a download file (in MB) and the speed of an Internet link (in Mbps), 
calculate and report the approximate download time of the file using this link (in minutes).'''


file_size = float(input('Insert the size of the file (MB):'))
internet_speed = float(input('Insert the velocity of your net (Mbps): '))
bit_to_byte = internet_speed / 8
download_time = (file_size / bit_to_byte) / 60
print(f'The download time will be {download_time:.2f}min')
