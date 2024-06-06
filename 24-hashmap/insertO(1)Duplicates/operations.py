import random
class RandomizedCollection:

    def __init__(self):
        self.hm = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        flag = None
        if val in self.hm:
            # If val is in th self.hm, the value of the set_ varibale is just whatever there in th self.hm related to that val.
            set_ = self.hm[val]
            flag = False
        else:
            # If val is not i self.hm, create a new set_
            set_ = set()
            flag = True
        # Assign to the value i self.hm either a new set_ or just add to the already existed set_.
        idx = len(self.nums)
        set_.add(idx)
        self.hm[val] = set_
        self.nums.append(val)
        return flag
        
    def remove(self, val: int) -> bool:
        if val in self.hm:
            set_ = self.hm[val]
        else:
            return False
        # Get the index of the val from dictionary's set_.
        remidx = set_.pop()
        # Assign the update set_ to the val
        self.hm[val] = set_
        if remidx==len(self.nums)-1:
            # If the removed index is same as the last index, simply remove that element from the list
            self.nums.pop()
        else:
            # Get the index of last element
            lastIdx = len(self.nums)-1
            # Swap the removed index with the last index (We want to move the element to be deleted ot the end of the list os that the operation can be done in O(1))
            # Save the value of last element in the list
            temp = self.nums[lastIdx]
            removedEle = self.nums[remidx]
            self.nums[remidx] = self.nums[lastIdx]
            self.nums[lastIdx] = removedEle
            # Remove the last element from the list
            self.nums.pop()
            # Remove the removed index from set_
            # Find where is the last element in the dictionary, update its index
            set_ = self.hm[temp]
            set_.remove(lastIdx)
            set_.add(remidx)
            # Assign to the dictionary, the new set_.
        # If all occurrence of a value is deleted, in another words, there is no index in the set_ related to that value, simply delete it from dictionary
        if not self.hm[val]:
            del self.hm[val]     
        return True  

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()