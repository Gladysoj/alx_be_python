size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    row + 1

    for col in range(size):
        print("*", end="")
        print()
        row += 1