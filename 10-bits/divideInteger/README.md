### Question:

### Idea-1:

Subtraction: subtract and keep the counts of how many times you are able to subtract until the results becomes negative.

#### Analysis:

`Time Complexity` is `O(Answer) it go up to (2^31)` as we are checking every element.
`Space Complexity` is `O(1)` as we are not using any additional spaces.

### Idea-2:

Set the ith Bit.

##### Handling Signs of the inputs.

Let's take an example with a = 12 and b = -3:

sign is initially 1.
a is positive, so sign remains 1.
b is negative, so sign is negated: sign = -1.
The division result is 12 // 3 = 4.
The final result should be -4 because a is positive and b is negative.

```py
  if sign < 0:
        answer = -answer
```

```py
class Solution:
    def divide(self, divisioned: int, divisor: int) -> int:
        sign = 1
        if divisioned < 0:
            sign = -sign
        if divisor < 0:
            sign = -sign
        divisioned = abs(divisioned)
        divisor = abs(divisor)
        temp = 0
        answer = 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i)) <= divisioned:
                answer = answer + (1 << i)
                temp = temp + (divisor << i)
        if sign < 0:
            answer = -answer

        if answer > 2**31 - 1:
            return 2**31 - 1
        elif answer < -(2**31):
            return -(2**31)
        else:
            return answer
```

#### Analysis:

`Time Complexity` is `O(32)=O(1)` as we are checking every element.
`Space Complexity` is `O(1)` as we are not using any additional spaces.
