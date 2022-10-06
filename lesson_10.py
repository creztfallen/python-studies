from ast import Try


def open_file():
    try:
        file = open('filee.txt')
        return True
    except Exception as err:
        print("Error: ", err)
        return False
    
while not open_file():
    print('Trying to open the file...')
    
print('File open!')        