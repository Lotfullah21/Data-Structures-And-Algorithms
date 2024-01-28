from collections import deque
q = deque()
# the base case for out palindrome
q.append("11")
q.append("22")
ans = ""
k = int(input("K: "))

def generateKthPalindrome(k):
    "add 1 and 2 at the end of the removed item each iteration."
    for i in range(k):
        tempAns = q.popleft()
        leftString = tempAns[:len(tempAns)//2]
        rightString = tempAns[len(tempAns)//2:len(tempAns)]
        # add 1 at the beginning and end.
        q.append(leftString + "11"+ rightString)
        # add to 2 at the beginning and the end.
        q.append(leftString + "22" + rightString)
    return tempAns

ans = generateKthPalindrome(k)
print("remnant queue",q)
print("removed element",ans)
        

# def generateKthPalindrome(k):
#     "add 1 and 2 to the end of a string at each line. this method will not give the palindrome numbers in order."
#     for i in range(k):
#         tempAns = q.popleft()
#         # add 1 at the beginning and end.
#         q.append("1" + tempAns + "1")
#         # add to 2 at the beginning and the end.
#         q.append("2" + tempAns + "2")
#     return tempAns

# ans = generateKthPalindrome(k)
# print("result",ans)
# print(q)
        