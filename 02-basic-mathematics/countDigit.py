def main():
    n = int(input("enter a number "))
    digit = int(input("enter a digit to count: "))
    print(countDigit(n,digit))
    
def countDigit(n,digit):
    count = 0
    while (n>0):
        rem = n%10
        if (rem==digit):
            count = count + 1
        print("n = ", n)
        n = n//10
        
    return count
        
if __name__ =="__main__":
    main()