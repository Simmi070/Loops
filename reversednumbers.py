number = input("Enter 2 to 5 numbers: ")
reversed_number = ""

for i in range(len(number) - 1, -1, -1):
    for j in range(1):   # Inner loop runs once
        reversed_number += number[i]

print("Original Number:", number)
print("Reversed Number:", reversed_number)