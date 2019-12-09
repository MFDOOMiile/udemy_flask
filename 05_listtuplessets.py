#List, Tuples, Sets
l = ["Raf", "Rafi", "Rafael"]
t = ("Raf", "Rafi", "Rafael")
s = {"Raf", "Rafi", "Rafael"}

print(l[0])
print(t[1])


#Modify list
l[0] = "Rafiki"         #cant modify tuples, sets
print(l)


#add to list
l.append("Rafiki")
print(l)


#removing from a list
l.remove("Rafi")
print(l)


#adding to sets - it's add, and not append, when working with sets. Append means "add at the end", but sets don't have an "end" since they don't have any order
