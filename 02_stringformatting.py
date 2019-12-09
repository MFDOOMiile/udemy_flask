#f-strings in python
name = "Bob"

print(f"Hello, {name}")

name = "Rafi"

print(f"Hello, {name}")


#Template strings with .format()
name = "Rafi"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)


longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format("Rafi", "Thursday")
print(formatted)