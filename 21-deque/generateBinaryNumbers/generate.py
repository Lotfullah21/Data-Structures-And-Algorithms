from collections import deque

def generate(N: int) ->None:
    "return the binary number for each N starting from 1 to N including N."
    q = deque()
    answer = []
    q.append("1")
    while N>0:
        removed = q.popleft()
        answer.append(removed)
        ele1 = str(removed) + "0"
        ele2 = str(removed) + "1"
        q.append(ele1)
        q.append(ele2)
        N-=1
    return answer
    
    
def main():
    N = 3
    result = generate(N)
    for i in result:
        print(i)
            
            
if __name__ =="__main__":  
    main()