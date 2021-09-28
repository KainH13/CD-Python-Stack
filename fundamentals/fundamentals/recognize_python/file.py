num1 = 42 # variable delcaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, list -> access value
pizza_toppings.append('Mushrooms') # list -> add value at end
print(person['name']) # log statement, dict -> access value
person['name'] = 'George' # dict -> change value
person['eye_color'] = 'blue' # dict -> add key value pair
print(fruit[2]) # log statement, tuple -> access value

if num1 > 45: # conditional
    print("It's greater") # log statement, string
else: # conditional
    print("It's lower") # log statement, string

if len(string) < 5: # conditional, length check
    print("It's a short word!") # log statement, string
elif len(string) > 15: # conditional, length check
    print("It's a long word!") # log statement, string
else: # conditional
    print("Just right!") # log statement, string

for x in range(5): # for loop
    print(x) # log statement, number
for x in range(2,5): # for loop
    print(x) # log statement, number
for x in range(2,10,3): # for loop
    print(x) # log statement, number
x = 0 # variable delcaration, number
while(x < 5): # while loop with exit condition
    print(x) # log statement, string
    x += 1 # changing a number variable

pizza_toppings.pop() # list -> removing a value
pizza_toppings.pop(1) # list -> removing the value at the index of 1

print(person) # log dictionary
person.pop('eye_color') # dict -> remove eye_color key and value
print(person) # log dictionary

for topping in pizza_toppings: # for loop - iterating through items in a list
    if topping == 'Pepperoni': # conditional - checking string equality
        continue # move to the next condition
    print('After 1st if statement')
    if topping == 'Olives': # conditional - checking string equality
        break # breaks out of the for loop if condition is true

def print_hello_ten_times(): # function declaration - no parameters
    for num in range(10): # for loop iterating through a range of numbers
        print('Hello') # log string 'Hello'

print_hello_ten_times() # calling function

def print_hello_x_times(x): # function declaration with 1 parameter
    for num in range(x): # for loop iterating through range of numbers
        print('Hello') # log string 'Hello'

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function declaration with 1 parameter and default value
    for num in range(x): # for loop iterating through range of numbers
        print('Hello') # log string 'Hello'

print_hello_x_or_ten_times() # function call with default value
print_hello_x_or_ten_times(4) # function call with specified value


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # variable declaration
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'