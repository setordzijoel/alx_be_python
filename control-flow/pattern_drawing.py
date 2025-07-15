size = int(input("Enter the size of the pattern: "))
i = 1

while i <= size:
    for j in range(1, size + 1):
        print("*", end="")

    print()
    i += 1