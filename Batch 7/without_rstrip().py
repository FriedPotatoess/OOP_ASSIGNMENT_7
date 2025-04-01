#Create a program that do the same functionality without using rstrip() function.

#Custom rstrip
def rstrip(user_input):
    index = len(user_input) - 1  
    while index >= 0 and user_input[index] == ' ':  
        index -= 1  
    return user_input[:index + 1]

#Takes user input
user_input = input("Enter your sentence: ")

#Prints the modified sentence
print(f'"{rstrip(user_input)}"')