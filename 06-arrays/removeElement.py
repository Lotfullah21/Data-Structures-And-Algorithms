def removeElement(nums: int, val: int) -> int:
    while val in nums:
        nums.remove(val)
            

n = list(map(int, input("").split()))
val = int(input("value = "))
print("after removal",removeElement(n,val))
print(n)