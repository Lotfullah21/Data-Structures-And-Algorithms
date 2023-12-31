class Solution:
    def rotate(self, arr:list, k:int) -> None:
        # reverse the whole array
        start = 0
        end = len(arr) - 1
        k = k%len(arr)
        while(start<end):
            # swap the elements
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start + 1
            end = end - 1 
            
        start = 0
        end = k - 1
        # 2nd loop to revers the first k elements
        while(start<end):
            # swap the elements
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start + 1
            end = end - 1 
            
        # to get the element after k rotation back to its normal position
        start = k
        end = k - 1
        while(start<end):
            # swap the elements
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start + 1
            end = end - 1 
        return arr


def main():
    input_str = input("Enter elements separated by commas: ")
    # Remove '[' and ']' from the input string
    input_str = input_str.replace('[', '').replace(']', '')
    arr = list(map(int, input_str.split(",")))
    k = int(input("K = "))
    solution = Solution()
    print(solution.rotate(arr,k))
    
    
if __name__ == "__main__":
    main()