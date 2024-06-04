import random

class RandomizedSet:
    def __init__(self):
        self.hm = {}
        self.nums = []


    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        else:
            self.nums.append(val)
            self.hm[val] = len(self.nums)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        else:
            # Find the index of the value in dictionary, it is best use of hashmap here, instead of iterating directly we have access to the index and easily we can swap it in list.
            idx = self.hm[val]
            # First delete from dictionary
            del self.hm[val]
            # Get the last index
            idx1 = len(self.nums)-1
            # Save the last items index
            temp = self.nums[idx1]
            if idx==len(self.nums)-1:
                self.nums.pop()
                return True
            else:
                # Swap the values at the index we want to delete and the last value
                firstVal = self.nums[idx1]
                self.nums[idx] = self.nums[idx1]
                self.nums[idx1] = firstVal
                # After swapping with the last index value, remove it
                self.nums.pop()
                # Update the index of last element with the index of removed element.
                self.hm[temp] = idx
                return True

    def getRandom(self) -> int:
        # Lists plays crucial in this operation, as we do not have this operation in dictionary.
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()