#If with in statements
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watch {user_movie} too!")
else: 
    print(f"I haven't watched {user_movie} yet!")

#Number game 
number = 7
user_input = input("Enter 'y' if you'd like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number: 
        print("You guessed correctly!!")
    elif abs(number - user_number) == 1:
        print("You were off by 1!")
    else:
        print("Sorry, You're way off!")