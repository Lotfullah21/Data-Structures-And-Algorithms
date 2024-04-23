class Deque:
    def __init__(self):
        self.items = []

    def push_back_pb(self, x):
        self.items.append(x)
        print(x)

    def push_front_pf(self, x):
        self.items.insert(0, x)
        print(x)

    def pop_back_ppb(self):
        if len(self.items) == 0:
            print(-1)
        else:
            self.items.pop()
            print(len(self.items))

    def front_dq(self):
        if len(self.items) == 0:
            print(-1)
        else:
            print(self.items[0])
            
# Sample Driver Code
if __name__ == "__main__":
    q = int(input().strip())
    deque = Deque()
    for _ in range(q):
        query = input().strip().split()
        if query[0] == "pb":
            deque.push_back_pb(int(query[1]))
        elif query[0] == "pf":
            deque.push_front_pf(int(query[1]))
        elif query[0] == "pp_b":
            deque.pop_back_ppb()
        elif query[0] == "f":
            deque.front_dq()
