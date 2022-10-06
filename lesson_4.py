names = ['Geralt', 'Dijkstra', 'Jarpen']
name = 'Mateus'
# int_list = range(0, 100, 2)

# for name in names:
#     print(name)
    

# for i in int_list:
#     print(i)    

# for i in range(len(names)):
#     print(names[i])
    
# for char in name:
#     print(char)    

# i= 1
# while i < 10:
#     print('i is still less than 10: ', i)
#     i += 1
    
# print('\nEnd of while: ', i)    

guests = int(input('How many people were invited to the party: '))

guest_list = []

i = 1
while i <= guests:
    guest_name = input('Guest #' + str(i) + ' name: ')
    guest_list.append(guest_name)
    i += 1