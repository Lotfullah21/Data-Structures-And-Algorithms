n, m = list(map(int, input().split()))
array = []
# Taking user input as a list for each row
for i in range(n):
    valid_input = False
    #  two attempts if there is error
    for _ in range(2):
        # print(f"Enter values for row {i + 1} ({m} elements, separated by space):")
        array_row = list(map(int, input().split()))
        if len(array_row) == m:
            valid_input = True
            break
        else:
            print(f"Error: Number of elements should match with {m} columns. Please try again.")

    if not valid_input:
        print(f"Exceeded maximum attempts for row {i + 1}. Exiting.")
        break  # Exit the outer for loop if maximum attempts are reached
    array.append(array_row)
# Print the array if it has been successfully filled
if len(array) == n:
    for i in range(n):
        for j in range(m):
            print(array[i][j],end=" ")
        print()
        # print(array[i])