<h2><a href="https://leetcode.com/problems/the-skyline-problem/description/"></a></h2>

The line currentH = -pq[0] if pq else 0 computes the current height of the skyline as follows:
When pq is not empty: The height of the tallest building (i.e., the current maximum height) is obtained by negating the smallest value in the min-heap (-pq[0]).

Time Complexity: O(nlogn) (with efficient heap operations) or

Space Complexity: O(n)
