class DirectAcessTable:
    def __init__(self, bucket):
        self.bucket = [0]*bucket
    def insert(self, i):
        self.bucket[i]=1
    def delete(self, i):
        if self.bucket[i]==1:
            self.bucket[i]=0
    def search(self, i):
        if self.bucket[i]==1:
            print(1)
            return 1
        else:
            print(-1)
            return -1
    def display(self):
        return self.bucket
        
        
table = DirectAcessTable(10)
table.insert(1)
table.insert(3)
table.insert(5)
result = table.display()
print(result)
table.search(5)
table.delete(2)
table.delete(3)
table.search(3)