

import math
def main():
    n = int(input(""))
    ans = perfect_square(n)
    if ans*ans == n:
        print("true")
    else:
        print("false")
    
def perfect_square(n):
    ans = 1
    i = 1
    while (i*i<=n):
        ans = i
        i = i + 1
    return math.floor(ans)


if __name__ == "__main__":
    main()
