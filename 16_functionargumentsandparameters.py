#Function Arguments and Parameters
def add(x, y):
    result = x +y
    print(result)

add(5, 3)

###~~~~~###

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Rafi", "Alvi")       #positional arguments
say_hello(surname="Rafi", name="Alvi")  #named/keyword arugments  

###~~~~~###

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You dumb dumb")

divide(dividend=15, divisor=0)  #try to always use named/keyword arguments, will make code easier to read. Positional arguments ALWAYS go first, followed by named/keyword arguments