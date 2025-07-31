import random
import string

lenght_defined = False
password_parts = []
password = ""

def user_choice():
    global choice , lenght_defined
    choice = input("\nY/N").lower()
    if choice == "y":
        print("Generating password...")
        lenght_defined = True
    if choice == "n":
        print("Aborting selection...")

while lenght_defined == False:
    try:
        lenght = int(input('Lenght(Minimum 8): '))
        if lenght < 8:
            print("Password would be too short. Do you wish to continue?")
            user_choice()
        elif lenght > 64:
            print("Password would be too big. Do you wish to continue?")
            user_choice()
        else:
            print("Generating password...")
            lenght_defined = True
    except ValueError:
        print("Please input a number!")
        pass    
for i in range(0 , lenght):
    if random.randint(1 , 3) == 1:
        password_parts.append(random.choice(string.ascii_letters))
    elif random.randint(1 , 3) == 2:
        password_parts.append(random.choice(string.punctuation))
    else:
        password_parts.append(random.choice(string.digits))
for parts in password_parts:
    password += parts
print(password)      