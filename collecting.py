# from collections import Counter

# list1 = ['x','y','z','x','x','x','y', 'z']

# Counter(list1)


from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
#print(Counter(list1))



list1.pop()
print(list1)


x = {'a': 5, 'b': 4}
y = {'c':6, 'd':8}


z = {**x,**y}
print(z)



class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

name = getattr(person, 'name')
print(name)

name2 = Student.name
print(name2)

name3 = person.name
print(name3)

marks = getattr(person, 'marks')
print(marks)

# Output: Sheeran
#         88