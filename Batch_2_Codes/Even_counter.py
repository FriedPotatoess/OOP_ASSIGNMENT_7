#Define the count of even numbers √
#Create the function to add every even number inputed to a count, then print the overall count √

even_count = 0

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_count += 1

print(even_count)
    



