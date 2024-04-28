# Generate Binary Representation:

Given an integer number N, generate all binary number for each integer from 1 to N.

#### Example:

Input: 2
Output: 1 10
Explanation: for N==1, binary representation is 1 and for N==2, binary representation is 10.

Input: 3
Output: 1 10 11
Explanation: for N==1, binary representation is 1 and for N==2, binary representation is 10 and for N==3, binary representation is 11.

### Idea-1:

Generate binary number for every N:

```py
def decimalToBinary(n: int):
    "Generates Binary number for integer n."
    binary = ""
    while n>0:
        binary = str(n%2)+binary
        n=n//2
    return binary

def generate(n):
    "Generates Binary representation for all integers from 1 to N."
    answer = []
    for i in range(1, n+1):
        answer.append(decimalToBinary(i))
    return answer

def main():
    N = 3
    result = generate(N)
    for i in result:
        print(i)

if __name__ =="__main__":
    main()

```

## Analysis:

The generate() function creates a list to store binary representations for each integer from 1 to N. This list has a length of N, so it requires O(N) space.
Inside the loop, the decimalToBinary() function constructs a binary string representation for each integer. The length of each binary string is roughly proportional to log(N), where N is the input value.

`Time Complexity:O(N \* log(N))`: The generate() function iterates from 1 to N, so it runs N times.
Inside the loop, the decimalToBinary() function is called for each value from 1 to N.

`Space Complexity:O(N \* log(N))`: Therefore, for each number from 1 to N, the space complexity of decimalToBinary() is O(log(N)).
Since decimalToBinary() is called N times in total, the overall space complexity becomes O(N \* log(N)).

### 1. Time Complexity Analysis:

- While Loop: The loop runs for N iterations.
  Inside the Loop:
  popleft() and append() operations on a deque are O(1).
  Constructing ele1 and ele2 takes O(1) time.

### 2. Space Complexity Analysis:

- Deque: The deque q can hold at most N elements.
- List: The list answer also holds N elements.

`Time Complexity`: O(N)
`Space Complexity`: O(N)

<h4><a href="https://www.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1?itm_source=geeksforgeeks">GFG</a></h4>
