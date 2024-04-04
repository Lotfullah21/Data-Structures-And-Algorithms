class myHash:
    def __init__(self, b: int):
        """creates a bucket of size b

        Args:
            b (int): size of the bucket.
        """
        self.BUCKET = b
        self.table = [[] for _ in range(self.BUCKET)]
        
    def insert(self, x):
        i = x%self.BUCKET
        self.table[i].append(x)
    def remove(self, x):
        i = x%self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)
    def search(self, x):
        i = x%self.BUCKET
        for ele in self.table:
            if x ==ele:
                return True
    def printElements(self):
        print(self.table)
       
        
            
myhash = myHash(12)
myhash.insert(1)
myhash.insert(3)
myhash.insert(5)
myhash.insert(9)
myhash.insert(11)
myhash.insert(19)
myhash.remove(19)
myhash.printElements()