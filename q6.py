num_rows = int(input("Enter the number of rows: "))

# Initialize the row number
row = 1

# Outer while loop to handle the rows
while row <= num_rows:
    # Initialize column number
    col = 1
    
    # Check if the row number is odd or even
    if row % 2 == 1:
        # For odd rows, print the row number repeated row times
        while col <= row:
            print(row, end=" ")
            col += 1
    else:
        # For even rows, print squares of the column numbers
        while col <= row:
            print(col**2, end=" ")
            col += 1

    # Move to the next line after each row
    print()

    # Move to the next row
    row += 1
