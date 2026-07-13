from  collections import ChainMap
student1 = {'name': 'Adihya', 'age': 20}
course1 = {'course': 'Python', 'grade': 'A'}
combined = ChainMap(student1, course1)
print(combined['name'])
print(combined['course'])
print(combined['grade'])