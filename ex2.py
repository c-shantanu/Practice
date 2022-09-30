### Task 1

person = {'name': 'Bart Simpson', 'address':'742 Evergreen Terrace' }
print(f'{person["name"]}, {person["address"]}')

### Task 2 

bart = {'name': 'Bart Simpson'}
homer = {'name':'Homer Simpson'}
address = {'address': '742 Evergreen Terrace'}

bart.update({'address': '742 Evergreen Terrace'})
homer.update({'address': '742 Evergreen Terrace'})

print(bart['address'])

### Task 3

ages = {'Peter':'36', 'Robin':'29', 'Michael':'33'}
for name, age in ages.items():
    print(f'{name} is {age}years old.')

### Task 4

animals = {'Alligator': '5', 'Tiger': '8', 'Parrot': '6', 'Hamster':'2', 'Dolphin':'7'}

#animals_to_remove = ('Alligator','Tiger', 'Hamster')

animals_to_remove =[]
for i in animals:
    if i [-1] == 'r':
        animals_to_remove += [i]  

for i in animals_to_remove:
    if i in animals:
        del animals[i]
print(animals)


transformer = ['a', 'u', 't', 'o', 'b', 'o', 't', 's']
print(''.join(transformer))

lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]
print(lists[0][1][0]['name']) 
print(lists[1][2]['age'])

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo'] 
#words.sort()
#words = words.sort()

# Replace range of elements 1 and 3, with “Lion”

words[1:4]= ['Lion']
print(words)





