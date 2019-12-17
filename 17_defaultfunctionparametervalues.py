#Default function parameter values
def add(x, y=10):
    print(x + y)

add(5)      #python uses default y value
add(5, 5)   #python relaced y's default value

###~~~~~##

default_y = 3

def add2(x, y=default_y):
    sum = x +y
    print(sum)

add2(2)

default_y = 4 
add2(2)