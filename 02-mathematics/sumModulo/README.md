### Question:

Given two numbers a and b, find the sum of a and b. Since the sum can be very large, find the sum modulo 10^8+7.

#### Integer Overflow

In many programming languages, there is a limit to the size of integers that can be stored. For example, in Python 3, integers can grow to arbitrary sizes, but in some other languages like C++ or Java, there are limits to the maximum value an integer can hold.

If the sum of two large numbers exceeds this maximum value, an integer overflow occurs. When an overflow happens, the number "wraps around" and may not give the correct result. This can lead to incorrect calculations and unexpected behavior in the program.

#### Modulo Operation to the Rescue

Taking the modulo of a number with a specific value keeps the result within a range, effectively "wrapping" the number around within that range.

In the case of the modulo the result is always in the range from 0 to 10^8+6 inclusive. So even if the sum of two large numbers is greater than 10^8+7 the result after taking the modulo will always be within this range.
