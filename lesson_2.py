# print('1.Escreve Geralt\n2.Escreve Yennefer\n3.Escreve Jaskier\n');

# opt = input('Escolha uma das oções acima:')

# if opt == '1':
#     print('\nGeralt')
# elif opt == '2':   
#     print('\nYennefer')
# elif opt == '3':
#     print('\nJaskier')
# else:
#     print('Opção Inválida')        

'''In python the logic operators !, &&, and || are not, and, and or respectively.'''

from ast import Num


age = int(input('Type your age:'))
weight = int(input('Type your weight:'))
height = float(input('Type your height:'))

if age >= 18 and weight >= 60 and height >= 1.70:
    print('You are able to join the army.')
else:
    print("You're not able to join the army.")    