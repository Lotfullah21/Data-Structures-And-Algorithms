# take the input from the user, convert it to sub strings based on the spaces,new line or tab. apply int to each of the substrings as we are expecting integers, at the end pack them inside a list
n = int(input(""))
arr = list(map(int,input().split()))
idx1, idx2 = map(int, input().split())

arr[idx1],arr[idx2] = arr[idx2],arr[idx1]

for x in arr:
    print(x,end=" ")
