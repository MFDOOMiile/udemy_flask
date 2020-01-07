###~~~Unpacking Keyword Arguments~~~###
def named(**kwargs):
    print(kwargs)               #method #1

named(name="Rafi", age=32)


###~~~###
def named_2(name, age):
    print(name, age)

details = {"name": "Rafi", "age": 32}       #method #2
named_2(**details)


###~~~###
def named_3(**kwargs):
    print(kwargs)

details_2 = {"name": "Rafi", "age": 32}     #method #3
named_3(**details_2)


###~~~###
def name(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    name(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
    
print_nicely(name="Rafi", age=32)


###~~~###
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Rafi", age=32)


###~~~###
"""
def post(url, data=None, json=None, **kwargs):
    return request("post", url, data=data, json=json, **kwargs)
"""             #pffff i didnt get this, no clue, skip for now

