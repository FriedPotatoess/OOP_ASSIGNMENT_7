#Create a program that do the same functionality without using rjust() function.

def rjust(user_input, width):
    if len(user_input) >= width:
        return user_input
    else:
        return ' ' * (width - len(user_input)) + user_input

# Gets the input and the supposed width of the input
user_input = input("Enter what you wanna enter: ")
width = int(input("How long should it be: "))

# Prints the padded input
print(f"'{rjust(user_input, width)}'")
