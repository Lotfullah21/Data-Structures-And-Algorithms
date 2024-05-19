class Solution:
    @staticmethod
    def count_sort(s):
        arr = list(s)
        maxChar = 'a'
        # Find the max value.
        for i in range(len(arr)):
            if arr[i] > maxChar:
                maxChar = arr[i]
        # -ord(`a`) to reduce the length of the array, and don't forget once adding it back when converting the int value when converting back to string.
        max_val = ord(maxChar) - ord('a')
        # Find the occurrence of each.
        count = [0] * (max_val + 1)
        for i in range(len(arr)):
            val = ord(arr[i]) - ord('a')
            count[val] += 1
        print(count, len(count))
        # Print the sorting.
        k = 0
        for i in range(max_val + 1):
            c = count[i]
            for j in range(c):
                arr[k] = chr(i + ord('a'))
                k += 1
        return ''.join(arr)

if __name__ == "__main__":
    s = input("Enter a string: ")
    result = Solution.count_sort(s)
    print(result)
