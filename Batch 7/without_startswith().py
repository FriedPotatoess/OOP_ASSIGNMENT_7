#Create a program that do the same functionality without using startswith() function.

#Custom starts with
def endswith(user_input, prefix):
    return user_input[:len(prefix)] == prefix

#Gets the input and the suffix
user_input = input("Please enter ya stuff: ")
prefix = input("Please enter the prefix you want to check: ")

#Tells you wether it starts with what prefix u entered
if endswith(user_input, prefix):
    print(f"The sentence starts with {prefix}")
else:
    print(f"The sentence does not end with {prefix}")
    
    
