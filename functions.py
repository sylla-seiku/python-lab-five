#Learning about Parameters
def greet_user(name): #the name function here is a prameter
    print(f'Hi {name}!')
    print('Welcome abpard')


print("Start")
greet_user("Seiku") # "Seiku" right here is an argument.
greet_user("Beyage")
print("Finish")

#diffirent example
def greet_user(first_name, last_name): #the name function here is a prameter
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abpard')


print("Start")
greet_user("Seiku", "Sillah") # "Seiku Sillah" right here is an argument.
print("Finish")

#practice inputting name with the great messege.
def greet_user(name):
    name = input("=>")
    print(f'Hi {name}!')
    print('Welcome abpard')

greet_user("")


'''
#Learning About Functions.
def greet_user():
    print('Hi there!')
    print('Welcome abpard')


print("Start")
greet_user()
print("Finish")
'''
