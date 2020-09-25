#cerner_2^5_2020 ## This code displays a multiplication table of a given number
number = input('Please type a number: ')
table_size = input('Please input a table size: ')
for i in range (1, int(table_size)+1):
    print ('{} x {} = {}'.format(number, i, int(number)*int(i)))
