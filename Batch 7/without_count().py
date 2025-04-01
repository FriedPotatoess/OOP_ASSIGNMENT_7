#Create a program that do the same functionality without using count() function.

#Custom definition for the count function
def count(user_input, word_in_search):
    word_count = 0
    i = 0
    
    while i < len(user_input):
        i = user_input.find(word_in_search, i)
        if i == -1:
            break
        word_count += 1
        i += len(word_in_search)
        
    return word_count

#Gets the user input and the word that the user wanna find and count
user_input = input("Enter a sentence: ")
word_in_search = input("Enter what word or character you wanna count: ")

#Outputs the word count 
print(f"The word '{word_in_search}' appears {count(user_input, word_in_search)} times in the sentence")