try:
    crystals = int(input("Enter the number of crystals: "))
    shields = int(input("Enter the amount of shields: "))
    result = crystals / shields
    print("Power distributed correctly", result)
except ZeroDivisionError:
    print("Do not distribute by 0")

except ValueError:
    print("Unexpected error")

except Exception as e:
    print("Error")

else:
    print("Succesfully distributed")

finally:
    print("System shutdown sequence logged")