def getEvenOdd(l):
    even = []
    odd = []
    for element in l:
        if element%2==0:
            even.append(element)
        else:
            odd.append(element)
    return even,odd

# Note: add space between input list while entering.

myList = list(map(int, input("Enter list of elements: ").split()))
even, odd = getEvenOdd(myList)
print("even list", even)
print("odd list", odd)