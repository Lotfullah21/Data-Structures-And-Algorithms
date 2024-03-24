#### Prime Factorization:

prime factorization of a number is the process of finding all prime numbers that can divide the given number.
when those factors multiplied, the original number is obtained.

#### Analysis:

`Time Complexity`

##### isPrime Function:

The isPrime function checks if a number n is prime.
It iterates through all numbers from 2 to the square root of n (inclusive), so it has a time complexity of O(sqrt(n)).

#### factorization Function:

The factorization function finds prime factors of the given number n.
It iterates through all numbers from 2 to n, so in the worst case, it has a time complexity of O(n).
For each number i in this range, it calls the isPrime function, which has a time complexity of O(sqrt(i)).
So, the overall time complexity of the factorization function can be considered as:

O(sqrt(n)) + O(n)\*O(sqrt(i)) = O(n)\*O(sqrt(i))
