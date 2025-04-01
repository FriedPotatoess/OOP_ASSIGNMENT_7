#Create a program that do the same functionality without using index() function.

def custom_index(user_input, word_in_search):
    # Iterate through the string to find the first occurrence of the substring
    for i in range(len(user_input) - len(word_in_search) + 1):
        if user_input[i:i+len(word_in_search)] == word_in_search:
            return i  # Return the index if substring is found
    raise ValueError(f"'{substring}' not found in the string")  # Raise an error if not found

# Get input from user
user_input = input("Enter a string: ")
word_in_search = input("Enter the substring to find: ")

# Call the custom_index function and handle exceptionsd
try:
    print(f"The first occurrence of '{word_in_search}' is at index {(custom_index(user_input, word_in_search))}")
except ValueError as e:
    print(e)
