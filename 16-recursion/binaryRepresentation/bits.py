def bits(n: int) -> bin:
    "Returns binary representation of an integer."
    if n==0:
        return 
    else:
        bits(n//2)
        print(n%2,end="")

        

def main():
    if __name__ == "__main__":
        n = int(input("Enter an integer: "))
        bits(n)
        
main()