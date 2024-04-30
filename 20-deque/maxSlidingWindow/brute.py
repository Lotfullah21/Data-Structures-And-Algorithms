def maxSlidingWindow(arr: list, k: int) -> list:
    window = []
    n = len(arr)
    for i in range(n-k+1):
        reference = arr[i]
        for j in range(i+1, i+k):
            reference = max(reference, arr[j])
        window.append(reference)
    return window


def main():
    arr = [1, 3,0,2,8, 9, 12]
    result = maxSlidingWindow(arr, 3)
    print("max sliding window =", result)

if __name__ == "__main__":
    main()