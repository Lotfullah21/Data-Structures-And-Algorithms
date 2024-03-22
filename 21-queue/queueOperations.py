class Solution:
    #Function to push an element in queue.
    def enqueue(self,q, x):
        q.append(x)

    #Function to remove front element from queue.
    def dequeue(self,q):
        if len(q) ==0:
            return -1
        x = q.pop(0)
        return x

    #Function to find the front element of queue.
    def front(self,q):
        if len(q)==0:
            return -1
        else:
            return q[0]
    def gear(self, q):
        if len(q)==0:
            return -1
        else:
            return q[-1]
    #Function to find an element in the queue.
    def find(self,q, x):
        if x in q:
            return True
        return False

solution = Solution()
q = [1, 2]
solution.enqueue(q,3)
solution.enqueue(q,4)
solution.dequeue(q)
front = solution.front(q)
gear = solution.gear(q)
searched = solution.find(q,4)

print("queue",q)
print("find",searched)
print("front",front)
print("gear",gear)
