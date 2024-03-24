#### Question:

Given an integer, count how many set bits it has?

#### Solution:

When a bit is ==1, we say that is a set bit.
The longest integer have 32 set bits (ones); 11111111111111111111111111111111.
2,147,483,647 and as low as -2,147,483,648 (stored as 32 bits).

We will do a `checkBit` operation for all bits of the given integer, if a bit is set, we add the count to the answer.

```py
 def checkBit(self, N, i):
    # If and operation is not == 0; remember, do not put it as N&(1<<i)==1: return True:, because if the bit is set, it does not mean it should be == 1.
        if N&(1<<i)!=0:
            return True
        else:
            return False
```

```py
    def setBits(self,N):
        ans = 0
        # Check For 32 integers.
        for i in range(32):
            # If not!=0, add the answer.
            if self.checkBit(N, i)==True:
                ans+=1
        return ans

```

#### Analysis

`Time Complexity` is `Olog(N)`, because number of bits in an integer is equal to `log(N)`; Here we are checking for all bits of an integer value.
`Space Complexity` is `O(1)`.
