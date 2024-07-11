#User function Template for python3


def find_greatest_number(a, b, c):
    # Write your code here
    firstMax = float("-inf")
    if a>=b and a>=c:
        firstMax = a
    elif c>=a and c>=b:
        firstMax = c
    else:
        firstMax = b
    return firstMax

ans = find_greatest_number(1,2,0)
print(ans)