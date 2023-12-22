class HashTable:
    def __init__(self):
        self.MAX = 6
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        ascii = 0
        for ele in key:
            ascii = ascii + ord(ele)
        ascii_val = ascii
        hashmap_value = ascii_val % self.MAX
        return hashmap_value
    
    # put at this key, this value
    def __setitem__(self, key, val):
        hash_val = self.get_hash(key)
        found = False
        # change the value of the key if an insertion made to the existed key.
        for idx, element in enumerate(self.arr[hash_val]):
            # check if the key is already existed in hash bucket.
            if len(element) == 2 and element[0] == key:
                self.arr[hash_val][idx] = (key,val)
                found = True
                break
        # if same key not found, added to the list. it evaluates to true when found is false
        if not found:
            self.arr[hash_val].append((key,val))  

        
    def __getitem__(self, key):
        hash_val = self.get_hash(key)
        # check for the elements in the particular hash value.
        for element in self.arr[hash_val]:
            # if first element of tuple is found
            if element[0] == key:
                # return the 2nd element in the tuple which is value associated with that key.
                return element[1]
    
    def delete_item(self, key):
        hash_val = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash_val]):
            # if the key is found.
            if key == element[0]:
                # delete that index.
                del self.arr[hash_val][idx]
    

table1 = HashTable()
table1["AI"] = "12 months"
table1["Machine Learning"] = "3 months"
table1["Deep learning"] = "3 months"
table1["Data Structure"] = "4 months"
table1["Front End"] = "3 months"
table1["Backend"] = "3 months"
table1["Cloud"] = "1 months"
table1["AI"] = "12 months"
table1.delete_item("AI")
print(table1.arr)
