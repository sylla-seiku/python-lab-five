#Learing Inheritance 
class Mammal:
     def walk(self):
        print("walk")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
   

class Dog(Mammal):
    def bark(self):
        print("bark")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()


'''
#Learning about constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)

#Practice creating a class for a person.
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")

seiku = Person("Seiku Sillah")
#print(seiku.name)
seiku.talk()

beyage = Person("Beyage Sillah")
beyage.talk()



#Learning About Classes
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

#learning about comments 
# I'm very familiar with comments so i didnot take any notes or write code on them.



#learning Exceptions
try:
    age = int(input('Age: '))
    print(age)
except ValueError: 
    print('Invalid value')

# in programing we use try except blocks to handle exceptions that are raised in our program.
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError: 
    print('Invalid value.')
    '''