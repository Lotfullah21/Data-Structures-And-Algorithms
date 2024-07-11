def main():
    n = int(input("Enter an integer for fast fib function: "))
    # print(fib(n))
    for i in range(n):
        print("fib of",i,"=",fib(i))
    newN = int(input("Enter a number for slower fib, better to be smaller than 40 if you don't want your ram to die: "))
    for i in range(newN):
        print("fib of",i,"=",slowfib(i))


def fib(n, memo={}):
    if n==0 or n==1:
        return n 
    try:
        return memo[n]
    except KeyError:
        answer = fib(n-1)+fib(n-2)
        memo[n] = answer
    return answer


def slowfib(n):
    if n<2:
        return n
    else:
        return slowfib(n-1)+slowfib(n-2)


if __name__ == "__main__":
    main() 
        