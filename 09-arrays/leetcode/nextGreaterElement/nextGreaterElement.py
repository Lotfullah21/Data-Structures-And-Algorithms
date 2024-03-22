class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert the integer to a string
        str_num = str(n)

        # Find the index of the first digit from the right that is smaller than the digit to its right
        idx = -1
        for i in range(len(str_num) - 2, -1, -1):
            if str_num[i] < str_num[i + 1]:
                idx = i
                break

        if idx == -1:
            return -1

        # Find the smallest digit to the right of idx that is greater than str_num[idx]
        val = str_num[idx]
        smallest = idx + 1
        for j in range(idx + 1, len(str_num)):
            if str_num[j] > val and str_num[j] <= str_num[smallest]:
                smallest = j

        # Swap the digits at idx and smallest
        str_num_list = list(str_num)
        str_num_list[idx], str_num_list[smallest] = str_num_list[smallest], str_num_list[idx]

        # Sort the digits to the right of idx in ascending order
        str_num_list[idx + 1:] = sorted(str_num_list[idx + 1:])

        # Convert the modified string back to an integer
        ans = int(''.join(str_num_list))

        # Check for overflow and return the result
        return ans if ans <= 2**31 - 1 else -1
