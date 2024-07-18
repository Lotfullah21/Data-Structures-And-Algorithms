n = 10
x = [0]*(n+1)
rank = [0]*(n+1)
for i in range(1,n+1):
    x[i] = i
    rank[i] = i
print(x)
print(list(range(n+1)))