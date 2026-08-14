while True
    print("===Loop Art Designer===")
    print("Choose a pattern to generate")
    print("1. Half pyramid pattern if stars.")
    print("2. Floyd's triangle.")
    print("3. Diamond pattern.")
    print("4. Exit")

    choice = int(input("Enter your choice 1, 2, 3, or 4: "))

    if choice==1:
       for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()