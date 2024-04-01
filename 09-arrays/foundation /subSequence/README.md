<a href="https://leetcode.com/problems/subsets/description/">leetcode</a>

`(1 << i)` creates a number where only the i-th bit is set to 1. This is used to create a mask for bitwise operations, such as checking if a specific bit is set in another number. In the checkBit function, this mask is then used to perform a bitwise AND operation with another number to check the state of the i-th bit.

If i = 0, (1 << i) results in 0b00000001.
If i = 1, (1 << i) results in 0b00000010.
If i = 2, (1 << i) results in 0b00000100.
If i = 3, (1 << i) results in 0b00001000.

So, when you call `checkBit(n, i)`, you pass in two arguments:

n: The number whose i-th bit you want to check.
i: The position of the bit you want to check, starting from the rightmost bit at position 0.
