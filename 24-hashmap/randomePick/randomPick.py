import random
from typing import List
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.hm = {}
        self.valid = n - len(blacklist)
        for i in range(len(blacklist)):
            self.hm[blacklist[i]] = -1
        for ele in blacklist:
            if ele<self.valid:
                while n-1 in self.hm:
                    n-=1
                self.hm[ele]=n-1
                n-=1
        
    def pick(self) -> int:
        num = random.randint(0, self.valid-1)
        if num in self.hm:
            return self.hm[num]
        else:
            return num

        

