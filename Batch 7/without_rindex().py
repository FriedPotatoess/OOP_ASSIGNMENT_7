#Create a program that do the same functionality without using rindex() function.

# Custom definition of the rindex function
def custom_rindex(user_input, word_in_search):
    for i in range(len(user_input) - len(word_in_search), -1, -1):
        if user_input[i:i+len(word_in_search)] == word_in_search:
            return i  
    raise ValueError(f"'{word_in_search}' not found in the string")  

# Get input from user
user_input = input("Enter a string: ")
word_in_search = input("Enter what word or character you wanna count: ")

# Print the last occurrence of the word that is searched for
try:
    print(f"The last occurrence of '{word_in_search}' is at index {custom_rindex(user_input, word_in_search)}")
except ValueError as e:
    print(e)
