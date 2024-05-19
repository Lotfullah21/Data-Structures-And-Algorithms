def logarithm(n: int) -> int:
    "Returns logarithm of a number."
    if n<=1:
        return 0
    else:
        return 1 + logarithm(n//2)
    
def main():
    if __name__ == "__main__":    
        n = int(input("Enter an integer: "))
        result = logarithm(n)
        print("logarithm of", n, "is", result)
        
main()