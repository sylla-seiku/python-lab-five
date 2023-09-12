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


'''
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