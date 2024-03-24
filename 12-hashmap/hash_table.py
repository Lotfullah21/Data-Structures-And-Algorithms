class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        ascii = 0
        for ele in key:
            ascii = ascii + ord(ele)
        ascii_val = ascii
        hashmap_value = ascii_val % self.MAX
        return hashmap_value
    
    def add_ele(self, key, val):
        hash_val = self.get_hash(key)
        self.arr[hash_val] = val
 
    def get_val(self, key):
        hash_val = self.get_hash(key)
        arr_val = self.arr[hash_val]
        return arr_val


table1 = HashTable()
print(table1.get_val("Salam"))
print(table1.arr)

