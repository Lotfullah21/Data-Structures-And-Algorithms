def FrequencyQueries(arr, queries):
    hm = {}

    for num in arr:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 1
    result = []
    
    for num in queries:
        if num in hm:
            result.append(hm[num])
        else:
            result.append(0)

    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    
    for _ in range(m):
        queries.append(int(input()))

    results = FrequencyQueries(arr, queries)
    for res in results:
        print(res)
