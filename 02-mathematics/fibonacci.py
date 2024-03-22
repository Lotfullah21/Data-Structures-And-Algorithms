def main():
    n = int(input("enter a number "))
    print(fibonacci(n))
    
def fibonacci(n):
    count = 0
    a = 0
    b = 1
    while (count<n):
        temp = b
        b = a + b
        a = temp
        count+=1
    return a
        
if __name__ =="__main__":
    main()