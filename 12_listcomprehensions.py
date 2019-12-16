#List Comprehensions
numbers = [1, 3, 5]
# doubled = []

# for num in numbers:
#     doubled.append(num * 2)       #for loop
#     print(doubled)
doubled = [x * 2 for x in numbers]  #list comprehension

print(doubled)


friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = []

# for friend in friends:
#     if friend.startswith("S"):                for loop
#         starts_s.append(friend)

starts_s = [friend for friend in friends if friend.startswith("S")]   #list comprehension

print(starts_s)