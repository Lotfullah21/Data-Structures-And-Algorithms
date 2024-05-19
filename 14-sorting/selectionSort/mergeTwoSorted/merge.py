def mergeTwoArrays(a: list, b: list) -> list:
    sizeA = len(a)
    sizeB = len(b)
    c = a[:] + b[:]
    c.sort()
    return c
a = [1, 2]
b = [0,-32]
result = mergeTwoArrays(a, b)
print(result)