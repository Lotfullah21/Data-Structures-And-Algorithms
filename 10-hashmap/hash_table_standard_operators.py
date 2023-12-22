class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        ascii = 0
        for ele in key:
            ascii = ascii + ord(ele)
        ascii_val = ascii
        hashmap_value = ascii_val % self.MAX
        return hashmap_value
    
    # put at this key, this value
    
    def __setitem__(self, key, val):
        # it gives us this functionality: arr["x"] = 122
        hash_val = self.get_hash(key)
        self.arr[hash_val] = val
        
    # it returns the value of a at index key
    def __getItem__(self, key):
        # it gives us functionality to search for a value in array arr["x"].
        hash_val = self.get_hash(key)
        arr_val = self.arr[hash_val]
        return arr_val
    
    def delete_item(self, key):
        hash_val = self.get_hash(key)
        self.arr[hash_val] = None


table1 = HashTable()
table1["AI"] = "12 months"
table1["Machine Learning"] = "3 months"
table1["Deep learning"] = "3 months"
table1["Data Structure"] = "4 months"
table1["Front End"] = "3 months"
table1["Backend"] = "3 months"
table1["Cloud"] = "1 months"
print('before deletion: ',table1.arr)
table1.delete_item("AI")
print("after deletion: ",table1.arr)