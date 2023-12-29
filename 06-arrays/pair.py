import time
import random

def maxPair(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = max(ans, arr[i] * arr[j])
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

    # Add optimizations and measure the time again
    # ...

if __name__ == "__main__":
    stress_test()
