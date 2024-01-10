import random
import time
def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    ans = maxPair(arr)
    print(ans)
    

def maxPair(arr):
    max_index1 = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[max_index1]:
            max_index1 = i

    max_index2 = 0
    for k in range(0, len(arr)):
        if k != max_index1 and (max_index2 == 0 or arr[k] > arr[max_index2]):
            max_index2 = k
# max_index2 == -1: This part checks whether max_index2 is still -1. This condition ensures that max_index2 is only updated when a valid candidate for the second maximum is found. 
# If max_index2 is still -1, it means that the current element at index k is the first element being considered as the second maximum.
    ans = arr[max_index1] * arr[max_index2]
    return ans

def stress_test():
    # Generate a large input dataset
    large_input = [random.randint(1, 1000) for _ in range(1000)]
    print(large_input)

    # Measure the time taken for the original implementation
    start_time = time.perf_counter()
    result_original = maxPair(large_input)
    end_time = time.perf_counter()
    print("Original implementation result:", result_original)
    print("Original implementation time:", end_time - start_time, "seconds")


if __name__ == "__main__":
    main()


# https://chat.openai.com/share/8cd7d042-6c80-4f0d-b032-ed6c989ec066