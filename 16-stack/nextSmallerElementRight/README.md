### Question:

Professor X wants his students to help each other in the chemistry lab. He suggests that every student should help out a classmate who scored less marks than him in chemistry and whose roll number appears after him. But the students are lazy and they don't want to search too far. They each pick the first roll number after them that fits the criteria. Find the marks of the classmate that each student picks.
Note: one student may be selected by multiple classmates.

```py

class Solution:
    def help_classmate(self,arr,n):
        stack = []
        answer = [-1]*n
        for i in range(n):
            while len(stack)>0 and arr[i]<arr[stack[-1]]:
                idx = stack.pop()
                answer[idx] = arr[i]
            stack.append(i)
        return answer
N = 4
arr = [1, 3, 2, 4]
solution = Solution()
result = solution.help_classmate(arr,N)
print(result)
[-1, 2, -1, -1]
Explanation:

1 does not have element greater than itself on right hand side, replace with -1.
or Roll number 1 has less marks and cannot pick the ones with higher marks to teach.

2 is smaller than 3, replace it with 2.
or 2nd student found some one who has less marks than his mark (2), so he will help the student with two marks.

last two student does not have some who scored less than them, so they are not choosing any one.
2 and 4 also does not have elements smaller than themselves on right hand side, replace with -1.

```

#### Analysis:

`Time Complexity` is `O(N)`, for each element, there is a finite number of possibilities, either replace, do not replace or replace and at max replace N element at last if previous could not.
`Space Complexity` is `O(N)` for stack space
