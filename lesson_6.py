# def sum(n1, n2):
#     return n1 + n2
    
# print(sum(48, 52))  

# def printHello():
#     print('Hello')  
    
# printHello()
   
   
# def has_seven_items(arg):
#     if len(arg) == 7:
#         return True
#     else: 
#         return False
    
# if has_seven_items('1234567'):
#     print('It really has seven items.') 

numbers = [9, 12, 34, 57, 2, 101, 3, 6, 87]

def max_min(collection):
    mx = max(collection)
    mn = min(collection)
    res = 'The maximum number is:' + str(mx) + '\nThe minimum number is:' + str(mn) 
    return res     

print(max_min(numbers))