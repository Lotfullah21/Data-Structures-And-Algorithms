# 1. Brute Force (Linear Search)
def main():
    array = list(map(int, input("Enter an array: ").split()))
    target = int(input("Enter an integer find the floor for: "))
    print(floor(array, target))
    
def floor(array, target):
    "Returns closest smaller number to the target target"
    n = len(array) 
    ans = float("-inf")
    for i in range(n):
        # If exact number is present, just return that.
        if array[i] == target:
            return target
        elif array[i]>ans and array[i]<=target:
            ans = array[i]       
    return ans
if __name__ == "__main__":
    main()