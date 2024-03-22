"""
for all even numbers, the last digit of its binary representation is == 0 
for all odd numbers, the last digit of its binary representation is == 1

2: 010
3: 101
4: 100
5: 101
6: 110
7: 111
    
to solve the question, we will check whether the last digit of a number is zero or one.

7&1:   111
       001
       ----
       001 => odd number
       
4&1:   100
       001
       ----
       000 => even number
       

to do so, we take use the bitwise and operation between the given number and one (number & 1)
which will result either to 1 or zero. if zero, it means that the last bit of the number is 0, and if 1, it means the last bit of the number is 1.
"""



def main():
    n = abs(int(input("Enter a number: ")))
    answer = is_even(n)
    print(answer)


def is_even(x):
    if ((x & 1) ==0):
        return f"{x}  is an even number"
    else:
        return f"{x} it is an odd number"
    

if __name__ == "__main__":
    main()

