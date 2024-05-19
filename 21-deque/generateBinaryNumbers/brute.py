def decimalToBinary(n: int):
    "Generates Binary number for integer n."
    binary = ""
    while n>0:
        binary = str(n%2)+binary
        n=n//2
    return binary

def generate(n):
    "Generates Binary representation for all integers from 1 to N."
    answer = []
    for i in range(1, n+1):
        answer.append(decimalToBinary(i))
    return answer

def main():
    N = 3
    result = generate(N)
    for i in result:
        print(i)
                        
if __name__ =="__main__":  
    main()