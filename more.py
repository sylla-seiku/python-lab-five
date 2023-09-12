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