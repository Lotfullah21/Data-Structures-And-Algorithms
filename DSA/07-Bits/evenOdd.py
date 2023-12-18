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

