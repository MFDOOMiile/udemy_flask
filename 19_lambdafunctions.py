###~~~Lambda Functions~~~###
def add(x, y):
    return x + y        #normal function

print(add(5, 7))


print((lambda x, y: x + y)(5, 7))     #function can be rewritten as a lambda like this

###~~~~~###

sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]     #this is more python
doubled = list(map(lambda x: x * 2, sequence))         #this is more other languages
print(doubled)