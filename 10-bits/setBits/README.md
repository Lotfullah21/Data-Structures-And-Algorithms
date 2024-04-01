### Question:

Given a number N and a value K. From the right, set the Kth bit in the binary representation of N. The position of Least Significant Bit(or last bit) is 0, the second last bit is 1 and so on.

### Solution:

Find a way to turn the Kth bit of N to 1, if that is zero.
to do so, we can use `or` operation.
For instance

```py
N=8; K=1;
Mean switch on the first bit of 8;
8 = 1000
Lets say 1000
         0010 => 1010, this is an add(or) operation.
So, simply add a mask and shift it `ith` position to the right and do the or operation with N.
```
