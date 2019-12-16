#Loops

#While Loop
number = 7

while True: 
    user_input = input("Enter 'y' if you'd like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))

    if user_number == number: 
        print("You guessed correctly!!")
    elif abs(number - user_number) == 1:
        print("You were off by 1!")
    else:
        print("Sorry, You're way off!")


#For Loop
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total = sum(grades)

print(total / amount)