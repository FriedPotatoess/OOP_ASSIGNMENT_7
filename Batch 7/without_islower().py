#Create a program that do the same functionality without using islower() function.

def islower(user_input):
    for char in user_input:
        if 'A' <= char <= 'Z':
            return False
    return True

#Gets user input
user_input = input("please enter all lowercase or you'll wake up the librarian and bad things will happen: ")

#Will tell you if the input is all lowercase or no
if islower(user_input):
    print("thankyou for your cooperation")
else:
    print("i told you to enter only lower case letters, now youre gonna get eaten.")

