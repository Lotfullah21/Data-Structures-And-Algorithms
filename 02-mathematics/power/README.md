#### Question:

Given the base and exponent, compute base to the power exponent.

Input: base = 3; exponent = 2
Output: 3\*3 = 9

#### Solution:

Base to power means multiply base, exponent times

#### Idea-1:

go up to exponent times and multiply the base that many time.

```py
def power(x, n):
    """
    Returns base to the power n
    """
    pow = 1
    for i in range(1, n+1):
        pow = pow * x
    return pow
```

#### Analysis:

`Time Complexity` is `O(N)`, because we are going through up to exponent.
`Space Complexity` is `O(1)` no extra space is used.

#### Idea-2:

Use recursive approach(ahead of time, later will be discussed in details).

x^n/2\*x^n/2 = x

#### Analysis:

`Time Complexity` is `O(logN)`, every time we are dividing the n with half.
`Space Complexity` is `O(logN)`, stack call space.
