### Time Complexity Analysis

1. **Loop Over Input String**: The function iterates over each character in the input string `s`. Let `n` be the length of the input string.

2. **Checking Vowels**: For each character, it checks if it is a vowel. This check involves looking up whether the character is in the `vowels` list. The `in` operator on a list has a time complexity of O(n), where n is the number of elements in the list. However, since `vowels` is a fixed list of length 5 (["e", "i", "o", "a", "u"]), this check is effectively constant time, or O(1).

3. **Appending to `new_list`**: Appending to a list in Python is also O(1) on average. In the worst case, where the list needs to resize its underlying array, it can be O(n), but on average it's considered O(1).

4. **Overall Time Complexity**: Combining these operations, we see that the loop runs `n` times, and within each iteration, the operations are all O(1) or constant time. So, the overall time complexity of the `countVowels` function is O(n).

In Big O notation, where `n` is the length of the input string `s`.
`Time Complexity`: `O(N)`; the time complexity of the `countVowels` function; This means that the time taken by the function to process the input string grows linearly with the size of the input.
