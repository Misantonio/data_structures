from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'rollNo'])

student1 = Student('Misael', 21, 4)

print(student1.name)
print(student1.age)
print(student1.rollNo)
print("")

student1 = student1._replace(name="Antonio") # replace works in a copy of student1
print(student1)
print(student1._fields)