##### Prime number:

A number is said to be a prime number if it is only divisible by one and itself. For instance 2 is divisible by 2 and 1.
by divisible we mean the reminder of two number is zero.

The numbers that are not prime are known as composite numbers.

`1` is the only number that is neither prime, nor composite.

#### Idea-1:

```py

  def isPrime(self, n: int) -> bool:
        "returns true if it is a prime number."
        if n==1:
            return False
        for i in range(2, n):
            if n%i==0:
                return False
        return True
```

#### Analysis:

`Time Complexity` is `O(N)` if the number is a prime number and we have to execute the loop `n` times.
`Space Complexity` is `O(1)` no extra space is used.

#### Idea-2:

The divisors of a number is always appears in pairs.

```py
2 = (1, 2); 2%1 ==0 and 2%1==0
3 = (1, 3); 3%1==0 and 3%3==0
4 = (1, 4), (2, 2); 4%1==0 and 4%2==0 and 4%4==0. not a prime number, because it has three divisors.
5 = (1, 5); 5%1==0 and 5%5==0.
6 = (1, 6), (2, 3)
7 = (1, 7)
8 = (1, 8), (2, 4). it has 4 divisors that can divide 8 completely which are 1, 8, 2 and 4.
9 = (1, 9), (3, 3)
10 = (1, 10), (2, 5)
11 = (1, 11)



```

```py

class Prime:
    def isPrime(self, n: int) -> bool:
        "returns true if it is a prime number."
        if n==1:
            return False
        for i in range(2, int(n**1/2)+1):
            if n%i==0:
                return False
        return True

```

#### Analysis:

`Time Complexity` is `O(sqrt(N))` if the number is a prime number and we have to execute the loop `sqrt(n)` times.
`Space Complexity` is `O(1)` no extra space is used.
