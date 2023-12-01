n = int(input(""))
newDigit = " "
if (n<0):
    n = n*-1
while (n>0):
    lastDigit = n%10
    print("new Digit",newDigit,"Last Digit",lastDigit)
    newDigit = str(newDigit) + str(lastDigit) 
    n = int(n/10)

print("Final Answer",newDigit)