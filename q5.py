# Accept the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Outer loop to handle the rows
for row in range(1, num_rows + 1):
    # Inner loop to handle the columns
    for col in range(1, row + 1):
        if row % 2 == 0:
            # Print the row number if it is even
            print(row, end=" ")
        else:
            # Print the column number if the row number is odd
            print(col, end=" ")
    # Move to the next line after each row
    print()
