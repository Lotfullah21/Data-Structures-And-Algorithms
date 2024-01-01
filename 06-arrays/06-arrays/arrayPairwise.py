import time
def main():
    # split method divide a string into substring based on space, s = "a b c",  s = "a" "b" "c"
    n = int(input(""))
    arr = list(map(int, input("").split()))
    ans = maxPair(arr)
    start_time = time.perf_counter()
    # Code to measure
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
    print(ans)

def maxPair(arr):
    ans = 0
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]*arr[j])>ans:
                print(arr[i],arr[j])
                ans = arr[i]*arr[j]
    return ans

if __name__ == "__main__":
    main()