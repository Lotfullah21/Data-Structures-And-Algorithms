class Prime:
    def isPrime(self, n: int) -> bool:
        "returns true if it is a prime number."
        if n==1:
            return False
        for i in range(2, n):
            if n%i==0:
                return False
        return True
    
    
    
# solution = Prime()
n = int(input("Enter an integer: "))
# result = solution.isPrime(n)
# if result:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")
    
    
list = [20,42, 76]
for ele in list:
    if n%ele ==7:
        print("yes", ele)