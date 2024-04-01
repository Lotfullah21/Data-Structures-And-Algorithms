
# we have a formula hcf * lcm = a * b




'''
Multiples of a number are obtained by multiplying that number by integers (positive or negative).
For example, the multiples of 3 are 3, 6, 9, 12, 15, 18, ... and so on.

Factors:
Factors of a number are the numbers that divide that number without leaving a remainder.
For example, the factors of 12 are 1, 2, 3, 4, 6, and 12.

For example, let's take 3 and 4. The multiples of 3 are 3, 6, 9, 12, 15, 18, ... and the multiples of 4 are 4, 8, 12, 16, 20, ... 
The common multiples are 12, 24, 36, ... and so on. The LCM is the smallest common multiple, which is 12.

'''

def highest_common_factor(x: int,y: int) -> int:
    smallest = min(x,y)
    hcf = 1
    for i in range(1, smallest + 1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf
    
def least_common_factor(x,y):
    lcm = (x*y) // (highest_common_factor(x,y))
    return lcm


def main():
    x,y = map(int, input("Enter x and y: ").split(" "))
    print(x,y)
    hcf = highest_common_factor(x,y)
    lcm = least_common_factor(x,y)
    print("hcf =",hcf,"lcm =",lcm)
    
if __name__ == "__main__":
    main()