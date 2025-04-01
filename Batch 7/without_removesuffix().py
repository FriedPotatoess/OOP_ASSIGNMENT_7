#Create a program that do the same functionality without using removesuffix() function.

#Fucntion for custom removesuffix
def remove_suffix(user_input, suffix):
    if user_input[:len(suffix)] == suffix:
        return user_input[len(suffix):]
    return user_input

#Gets the input and the prefix that is wished to be removed
user_input = input("Input your stuff: ")
suffix = input("Input which suffix you wanna remove: ")

#Outputs the input without the suffix
print(remove_suffix(user_input, suffix))