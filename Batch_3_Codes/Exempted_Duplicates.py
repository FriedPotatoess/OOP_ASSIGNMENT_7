#GOAL:Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#Place to store the inputed numbers and the code to ask for the user to input 10 numbers


print("Please input 10 numbers")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

#List for numbers without duplicate and first instance of duplicate numbers
unique_numbers