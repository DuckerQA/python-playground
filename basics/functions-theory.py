# 1. Use def to define a function

def hello():
    print("Hello, World!")
hello()

# The f"{name}" syntax in Python is similar to  `${}` in JavaScript/TypeScript for string interpolation.

def greet(name):
    print(f"Hello, {name}!")
greet('Mathew')

# 2. return works same as for other programming languages

def add(a, b):
    return a + b
add(100, 15)

# 3. to declare default value 

def greetCustomName(name="Guest"):
    print(f"Hello, {name}!")
greetCustomName()

# 4. Order matters in positional arguments

def person_info(name, age):
    print(f"{name} is {age} years old.")
person_info(25, "Alice")
#person_info(age=25, name="Alice")   <--- trick to workaround 🎯


# 5. *args Non-Keyword Arguments collects all positional arguments into a tuple

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4)) 

# 6. **kwargs collects keyword arguments into a dictionary.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, country="USA")

# 7. Lambda Functions - just short function with many arguments but one expression

add = lambda a, b: a + b
print(add(3, 5))

# its equal to 

def add2(a,b):
    return a + b
print(add2(3, 5))  

# 8 Scope - Global, local, nonlocal

#Basic
x = 10  
def my_function():
    print(x)  
my_function() 

#Global

y = 10
def update():
    global y  # Declaring x as global
    x = 20
update()
print(x)  # Output: 20

#Nonlocal - to overwrite the X lvl above 

def outer():
    x = "outer"
    def inner():
        nonlocal x  # Refers to x in the outer function
        x = "inner"
    inner()
    print(x)  # Output: inner

outer()