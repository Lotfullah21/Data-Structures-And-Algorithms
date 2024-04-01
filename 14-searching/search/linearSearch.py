def main():
    arr = list(map(int, input("Enter an array: ").split()))
    k = int(input("Enter the element you are looking: "))
    search = linearSearch(arr,k)
    if search:
        print("true")
    else:
        print("false")
    
    
def linearSearch(array: list, target: int) -> bool:
    "Returns True if the target is  present in the array."
    n = len(array)
    for i in range(n):
        if target == array[i]:
            return True
    
    
if __name__ == "__main__":
    main()
# Sample Input: 1 2 3 4 5 6 
# sample target: 4 
# Output: true 
    