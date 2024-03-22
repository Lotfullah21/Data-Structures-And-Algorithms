def fibonacci_loop(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
result = fibonacci_loop(10)
print(result)



# using while loop
n = int(input("Enter a number: "))
a = 0
b = 1
count = 0
while (count<n):
    temp = b
    b = a + b
    a = temp
    count+=1
print(a)


