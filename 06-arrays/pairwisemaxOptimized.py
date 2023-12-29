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

    max_index2 = -1
    for k in range(0, len(arr)):
        if k != max_index1 and (max_index2 == -1 or arr[k] > arr[max_index2]):
            max_index2 = k

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

