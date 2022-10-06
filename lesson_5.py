list = ['Monkey', 'Tiger', 'Dragon'] # List (is ordered)
_tuple = ('Monkey', 'Tiger', 'Dragon') # Tuple (fixed number of items)
_dic = {'name': 'Mateus', 'age': 24} # Dic(tionary)
_set = {'Monkey', 'Tiger', 'Dragon'} # Set


if 'Monkey' in _tuple:
    print('There is a monkey in the tuple.')
    
if 'Mateus' in _dic.values():
    print('Mateus is in the dictionary.')     
    
print(_dic.keys())
print(_dic['name'])    

_dic['name'] = 'Beyza'
print(_dic['name']) 

_dic['address'] = 'Any Avenue'
print(_dic)

_dic.clear()