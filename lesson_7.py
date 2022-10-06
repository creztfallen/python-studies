import sys

arguments = sys.argv

# print(arguments)


def sum(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2



if arguments[1] == 'sum':
    res = sum(float(arguments[2]), float(arguments[3]))
elif arguments[1] == 'minus':
    res = minus(float(arguments[2]), float(arguments[3]))
    
print(res)    