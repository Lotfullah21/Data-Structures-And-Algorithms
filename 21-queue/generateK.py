"""
generate a kth element which contains only 1 or 2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
correct choices: 1,2, 11, 12, 21, 21, 111, 112, 121, 122, 211, 212, 221, 222

Every time, remove a str from left most, and append to the removed number 1, and 2, and appended to the deque. 
Continue till kth iteration, and the removed element at that iteration is the answer.
"""


from collections import deque

k = int(input("Enter K: "))
q = deque()
q.append("1")
q.append("2")
ans = ""
def generateKtOneAndTwo(k):
    for i in range(k):  
        currAns = q.popleft()
        ans = currAns
        q.append(currAns + "1")
        q.append(currAns + "2")
    return ans
            
result = generateKtOneAndTwo(k)
print("result", result)
print(q)



def FrequencyQueries(arr, queries):
    freqMap = {}

    for num in arr:
        if num in freqMap:
            freqMap[num] += 1
        else:
            freqMap[num] = 1

    result = []
    for num in queries:
        if num in freqMap:
            result.append(freqMap[num])
        else:
            result.append(0)

    return result
