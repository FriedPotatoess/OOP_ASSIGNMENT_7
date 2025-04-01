#Create a program that do the same functionality without using zfill() function.

#Function for the custom zfill
def zfill(user_input, width):
    if len(user_input) >= width:
        return user_input
    else:
        return '0' * (width - len(user_input)) + user_input
    
#Takes the input and the supposed width
user_input = input("Input words or sentence: ")
width = int(input("How long should the characters be?: "))

#Prints the input with the zeroes required
print(zfill(user_input, width))

