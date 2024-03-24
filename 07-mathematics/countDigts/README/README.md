#### Question-1:

Given an integer N, count number of digits in the given integer.

Input: N = 12392
Output: 5, since 5 digits are present.

### Solution:

Divide the integer by 10, every time we divide an integer by 10, the last digit of that integer is removed; So, start dividing the integer by 10 until the integer becomes 0.
at every division, add 1 one to the total count.

#### Question-2:

Given an integer N, count number of digits in the given integer.

Input: N = 5
Output: 3, since in factorial of 5 which is 120, 3 digits are present.

### Solution:

First find the factorial of integer N and pass it to the function we wrote on question one to count the digits.
Divide the integer by 10, every time we divide an integer by 10, the last digit of that integer is removed; So, start dividing the integer by 10 until the integer becomes 0.
at every division, add 1 one to the total count.
