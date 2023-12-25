def is_odd(x: int) -> bool:
    if x%2 !=0:
        return True
    else:
        return False


x = [1,2,3,5,6,7,5,2,3,1,90,32,12,21,23,29]

odd_numbers = filter(is_odd,x)
print(odd_numbers)

for odd in odd_numbers:
    print(odd)