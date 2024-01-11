N = int(input("Enter a number: "))
newDigit =  ""
if (N<0):
    N = N * -1
while(N>0):
    # it will always gives the last digit as a remainder
    lastDigit = N%10
    newDigit = int(str(newDigit) + str(lastDigit)) 
    
    print("last digit",lastDigit, "new digit",newDigit)
    # int(N/10) removes the last digit which returns only int digits, and the last digit will be on the other side of the decimal
    N = N//10
print("new digit",newDigit)