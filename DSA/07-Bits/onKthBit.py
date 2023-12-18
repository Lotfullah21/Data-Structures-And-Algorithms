def main():
    n = int(input("Enter the number: "))
    k = int(input("Enter the position: "))
    print(onKthBitNum(n,k))
    
    
    
def onKthBitNum(n, k):
    ans = n | (1<<k)
    return ans
    

if __name__ == "__main__":
    main()