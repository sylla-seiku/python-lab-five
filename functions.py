#learning about Return Statements.
def square(number):
    return number * number

#result = square(3)
#print(result)
# or we can simply make the code shorter by runing an argument instead of making it into a variable.
print(square(3))


'''
#learning About Keyword and Positional Arguments.
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abpard')


print("Start")
greet_user("Sillah", "Seiku") # " 'Seiku' 'Sillah' here is considered a positional argument". so the position or order matters.
greet_user(last_name="Sillah", first_name="Seiku") # this example here is known as a keyword argument ans the positioning and order doesnt matter.
#if one is going to mix keyword and positional argumeants together it is best to use the positional followed by the keyword argument.
print("Finish")



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



#Learning About Functions.
def greet_user():
    print('Hi there!')
    print('Welcome abpard')


print("Start")
greet_user()
print("Finish")
'''
