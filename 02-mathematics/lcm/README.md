### Question:

Find the lowest number that can divide a and b.

Example: `lcm` of `6` and `4` is `12`, because it can divide both of them. 12/6=2 and 12/4=3

if both of the numbers are prime numbers, lcm will be multiplication of those prime numbers.

For example. lcm of 7 and 3 is 21

#### Solution:

The checking is done from `2` to `n`, but not including `n`. If in between any `n` is divisible by `i` other than itself, we say it is not a prime number.

It is guaranteed that any number is divisible by itself.

```py
class Prime:
    def isPrime(self, n: int) -> bool:
        "returns true if it is a prime number."
        if n==1:
            return False
        for i in range(2, n):
            if n%i==0:
                return False
        return True

```
