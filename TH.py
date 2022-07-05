name = input("please insert your name: ")
if name != "Taha":
    print("Welcome!")
    age = input("please insert your age: ")
    age = int(age)
    if age < 18:
        print("Sorry, you are not allowed enter!")
    else:
        print("Welcome!")

else:
    print("Sorry, you are not allowed enter!")

