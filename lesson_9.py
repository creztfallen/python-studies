#methods: r - read
# w - write, creates the file if there is none or overrite if exists
# r+ - read and write
# a - append, append things to the doc
# b - bytes, open byte files

file = open('file.txt', 'r') 

for i in range(1, 1001):
    file.write(str(i)+ "\n")

