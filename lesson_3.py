sentence = 'Hi, how are you doing?'

names_list = ['Geralt', 'Dijkstra', 'Jarpen']
fruits_list = ["Banana", "Apple", "Kiwii", "Pineapple"]

names_list.append('Jaskier')
names_list[0] = "Triss"
names_list.pop(1)
names_list.remove('Jaskier')
names_list.reverse()
names_list.sort()
names_list.insert(1, "Yennefer")
names_list.extend(fruits_list)



index = names_list.index("Jarpen")
copy = names_list.copy()
count = names_list.count('Geralt')

names_list.clear()

# print(sentence[0:23:2])
# print(sentence[::-1]) Reverse method (?gniod uoy era woh ,iH)
print(names_list)
print("Index:", index)
print("Copy:", copy)
print("Count:", count)