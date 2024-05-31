<h2><a href="https://leetcode.com/problems/brick-wall/">leetcode-554</a></h2>

```py
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0:0}
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total+=brick
                countGap[total] = 1 + countGap.get(total, 0)
        ans = len(wall)-max(countGap.values())
        return ans


```

```plaintext
wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]


```

```plaintext
countGap:
{
    0: 0,
    1: 3,
    2: 1,
    3: 3,
    4: 4,
    5: 2
}

```

## Analysis:

`Time Complexity`: `O(lamp+queries)`.
`Space Complexity`: `O(lamp)`, for every lamp, space has been used in dictionary.
'
