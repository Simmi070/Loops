base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent(must be a positive integer):"))

result = 1
for i in range(exponent):
    result = result * base

print(f"{base} raised the power of {exponent} is: {result}")