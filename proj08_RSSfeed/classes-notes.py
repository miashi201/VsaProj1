# Classes

# defining a class called Person, which is a type of object
class Person(object):
            ## METHODS ##

        #Inititalize#
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.living = True
    #other methods
    def update_age(self):
        self.age = self.age = 1

    #accssor method
    def get_age(self):
        return self.age
#creating a Person
p1 = Person("Mia Shines", 17)
print p1.get_age()
print p1.name

p1.living = False
print p1.living

## Sub Classes ## - does all the methods of the original class, no need to add code

#creat, subclass
class Student(Person):

    def set_grade(self, grade) :
                   self.grade = grade
    def years_until_graduate(self):
        return 13 - self.grade
s1 = Student(" Joe highSchool", 16)
s1.set_grade(11)
print s1.years_until_graduate()
import string
print string.punctuation