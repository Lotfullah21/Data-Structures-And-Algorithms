## Random Pick with Blacklist

You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

Implement the Solution class:

Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

<h2><a href="https://leetcode.com/problems/random-pick-with-blacklist/">leetcode-710</a></h2>

# Intuition

Given the range, we can see the output would an integer in the range(0,n-1).
Now, our task it to make the elements in the range consecutive even in the presence of black list integers, How?
By calculating the number of valid numbers and drawing a boundary, map each black list number to the non-black list number below that boundary.

# Approach

- Create a hashmap and variable to keep the number of valid numbers.
- Count how many valid numbers do we have that can be returned in this range, it can be calculated using given formula
- `valid points = (n-0+1) - len(black list)`; (n-0+1), because the starting point is 0 and ending is n, in this range we are having (n-0+1) elements.
- Put all elements from the black list into the hm, having numbers as key and a dummy value as a value for that number.
- Now, run a loop to replace all black list numbers that are coming before that valid number boundary.
- But, check if the blacklist's number is less than valid point
  - Run another loop to check if the value we want map to the blacklist number in the dictionary itself is not a black list number.
    - reduce the number n until it is not a black list number
    - Once reached to that value, map it to the dictionary and keep as the value of black list number.
- At the end, pick a random integer
  - If that integer is in the dictionary
    - return the value assigned to that integer in our dictionary
  - else, return the number itself.

# Complexity

- Time complexity:
  O(N)

- Space complexity:
  O(N)
