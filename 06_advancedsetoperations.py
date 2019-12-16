#Advance Set Operations

#difference - finding the difference between 2 diff sets
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends = abroad.difference(friends)
print(local_friends)

#union - combining sets
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)

#intersection - finding common items in 2 diff sets
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)